import os
import urllib.parse
import urllib.request
from typing import Optional, List
from datetime import datetime

import markdown
from ipywidgets import Image

from mlflow.entities import ViewType
from mlflow.server import ARTIFACT_ROOT_ENV_VAR
from mlflow.store.tracking import SEARCH_MAX_RESULTS_DEFAULT
from mlflow.tracking import MlflowClient

from flown import utils
from flown.api.wrapper_for_notebook import notebook_api
from flown.utils import merge_html

_client = MlflowClient()
_md = markdown.Markdown()


@notebook_api
def list_experiments(view_type=ViewType.ACTIVE_ONLY, restricted: bool = False, display_id: str = None):
    experiments = _client.list_experiments(view_type=view_type)
    experiments_data = [
        dict(name=exp.name,
             experiment_id=exp.experiment_id,
             lifecycle_stage=exp.lifecycle_stage,
             artifact_location=exp.artifact_location,
             artifact_console_url=utils.to_browsable_url(exp.artifact_location, is_obj=False),
             tags=exp.tags
             )
        for exp in experiments
    ]
    return merge_html(template_name='experiment_list.html',
                      params={'experiments': experiments_data},
                      display_id=display_id)


@notebook_api
def disp_experiment(experiment_id: str,
                    run_view_type: int = ViewType.ACTIVE_ONLY,
                    max_results: int = SEARCH_MAX_RESULTS_DEFAULT,
                    order_by: Optional[List[str]] = None,
                    page_token: Optional[str] = None,
                    restricted: bool = False,
                    display_id: str = None
                    ):
    return _disp_experiment(experiment_id,
                            run_view_type=run_view_type,
                            max_results=max_results,
                            order_by=order_by,
                            page_token=page_token,
                            restricted=restricted,
                            display_id=display_id)


def _disp_experiment(experiment_id: str,
                     run_view_type: int = ViewType.ACTIVE_ONLY,
                     max_results: int = SEARCH_MAX_RESULTS_DEFAULT,
                     order_by: Optional[List[str]] = None,
                     page_token: Optional[str] = None,
                     restricted: bool = False,
                     display_id: str = None
                     ):
    exp_info = _client.get_experiment(experiment_id=experiment_id)
    exp_info_data = dict(experiment_id=exp_info.experiment_id,
                         name=exp_info.name,
                         artifact_location=exp_info.artifact_location,
                         artifact_console_url=utils.to_browsable_url(exp_info.artifact_location, is_obj=False),
                         tags=exp_info.tags,
                         note=exp_info.tags.get('mlflow.note.content', ''),
                         note_html=_md.convert(exp_info.tags.get('mlflow.note.content', '')),
                         )

    run_infos = _client.list_run_infos(experiment_id=experiment_id,
                                       run_view_type=run_view_type,
                                       max_results=max_results,
                                       order_by=order_by,
                                       page_token=page_token,
                                       )
    run_infos_data = []
    for run in run_infos:
        detail = _client.get_run(run_id=run.run_id)
        data = dict(run_uuid=run.run_uuid,
                    run_id=run.run_id,
                    run_name=detail.data.tags.get('mlflow.runName', None),
                    parent_run_id=detail.data.tags.get('mlflow.parentRunId', None),
                    experiment_id=run.experiment_id,
                    user_id=run.user_id,
                    status=run.status,
                    start_time=datetime.fromtimestamp(run.start_time / 1e3),
                    end_time=datetime.fromtimestamp(run.end_time / 1e3),
                    artifact_uri=run.artifact_uri,
                    artifact_console_url=utils.to_browsable_url(run.artifact_uri, is_obj=False),
                    lifecycle_stage=run.lifecycle_stage,
                    detail=detail,
                    children=[]
                    )
        run_infos_data.append(data)

    # parameter
    run_params_set = set()
    run_metrics_set = set()
    for run in run_infos_data:
        detail = run['detail']
        run_params_set = run_params_set | set(detail.data.params.keys())
        run_metrics_set = run_metrics_set | set(detail.data.metrics.keys())

    # 階層構造を作る
    run_map = {run['run_id']: run for run in run_infos_data}
    root_runs = []
    for run in run_infos_data:
        parent_id = run['parent_run_id']
        if not parent_id:
            root_runs.append(run)
        else:
            parent_run = run_map[parent_id]
            parent_run['children'].append(run)

    # インデント情報を付与した1次元のリストにする（描画しやすいように）
    def set_generation_index(total_list, current_index, current_list):
        for parent in current_list:
            parent['generation_index'] = current_index
            total_list.append(parent)
            set_generation_index(total_list, current_index + 1, parent['children'])

    indexed_list = []
    set_generation_index(indexed_list, 0, root_runs)

    return merge_html(template_name='experiment_detail.html',
                      params={'exp_info': exp_info_data,
                              'run_infos': indexed_list,
                              'param_keys': sorted(list(run_params_set)),
                              'metrics_keys': sorted(list(run_metrics_set)),
                              },
                      display_id=display_id)


@notebook_api
def disp_run(run_id: str,
             artifact_path: str = None,
             restricted: bool = False,
             display_id: str = None
             ):
    return _disp_run(run_id=run_id,
                     artifact_path=artifact_path,
                     restricted=restricted,
                     display_id=display_id)


def _disp_run(run_id: str,
              artifact_path: str = None,
              restricted: bool = False,
              display_id: str = None
              ):
    # 選択されたrunの情報を取得
    run = _client.get_run(run_id=run_id)
    run_info = run.info
    run_data = dict(run_uuid=run_info.run_uuid,
                    run_id=run_info.run_id,
                    run_name=run.data.tags.get('mlflow.runName', None),
                    parent_run_id=run.data.tags.get('mlflow.parentRunId', None),
                    experiment_id=run_info.experiment_id,
                    user_id=run_info.user_id,
                    status=run_info.status,
                    start_time=datetime.fromtimestamp(run_info.start_time / 1e3),
                    end_time=datetime.fromtimestamp(run_info.end_time / 1e3),
                    artifact_uri=run_info.artifact_uri,
                    artifact_console_url=utils.to_browsable_url(run_info.artifact_uri, is_obj=False),
                    lifecycle_stage=run_info.lifecycle_stage,
                    tags=run.data.tags,
                    note=run.data.tags.get('mlflow.note.content', ''),
                    note_html=_md.convert(run.data.tags.get('mlflow.note.content', '')),
                    params=run.data.params,
                    metrics=run.data.metrics,
                    artifacts=[dict(path=a.path, file_size=a.file_size, is_selected=(a.path == artifact_path))
                               for a in _client.list_artifacts(run_id=run_id)],
                    )

    # 選択されたアーティファクトのビューワHTMLを生成
    if artifact_path:
        selected_artifact_html = merge_html('artifact_viewer.html',
                                            dict(artifact_path=artifact_path))
    else:
        selected_artifact_html = ''

    # runにひもづく実験の情報を取得
    exp_info = _client.get_experiment(experiment_id=run_info.experiment_id)
    exp_info_data = dict(experiment_id=exp_info.experiment_id,
                         name=exp_info.name,
                         artifact_location=exp_info.artifact_location,
                         artifact_console_url=utils.to_browsable_url(exp_info.artifact_location, is_obj=False),
                         tags=exp_info.tags,
                         note=exp_info.tags.get('mlflow.note.content', ''),
                         note_html=_md.convert(exp_info.tags.get('mlflow.note.content', '')),
                         )
    Image()

    return merge_html(template_name='run_detail.html',
                      params={'exp_info': exp_info_data,
                              'run_data': run_data,
                              'selected_artifact_html': selected_artifact_html
                              },
                      display_id=display_id)


@notebook_api
def markdown_editor(note_type: str, note_id: str,
                    restricted: bool = False,
                    display_id: str = None
                    ):
    if note_type == 'run':
        run = _client.get_run(run_id=note_id)
        markdown_str = run.data.tags.get('mlflow.note.content', '')
    elif note_type == 'exp':
        exp = _client.get_experiment(experiment_id=note_id)
        markdown_str = exp.tags.get('mlflow.note.content', '')

    return merge_html(template_name='markdown_editor.html',
                      params={'note_type': note_type,
                              'note_id': note_id,
                              'markdown_str': markdown_str,
                              },
                      display_id=display_id)


@notebook_api
def update_experiment_note(experiment_id: str, note_str: str,
                           restricted: bool = False,
                           display_id: str = None
                           ):
    _client.set_experiment_tag(experiment_id=experiment_id,
                               key='mlflow.note.content',
                               value=note_str)
    return _disp_experiment(experiment_id, restricted=restricted, display_id=display_id)


@notebook_api
def update_run_note(run_id: str, note_str: str,
                    restricted: bool = False,
                    display_id: str = None
                    ):
    _client.set_tag(run_id=run_id,
                    key='mlflow.note.content',
                    value=note_str)
    return _disp_run(run_id, restricted=restricted, display_id=display_id)


# uriをOS任せ（ブラウザなど）で開く。 画面更新なしなので @notebook_api で修飾しない。
def startfile(uri: str, restricted: bool = False, display_id: str = None):
    if uri.startswith('http:') or uri.startswith('https:') or uri.startswith('ftp:'):
        os.startfile(uri)
    else:
        path = urllib.parse.urlparse(uri).path if uri.startswith("file:") else uri
        path = urllib.request.url2pathname(path)
        os.startfile(path)


def set_default_artifact_uri_root(default_artifact_root: str):
    os.environ[ARTIFACT_ROOT_ENV_VAR] = default_artifact_root


@notebook_api
def text_editor(text_type: str, entity_id: str,
                    restricted: bool = False,
                    display_id: str = None
                    ):
    if text_type == 'run_name':
        run = _client.get_run(run_id=entity_id)
        text_value = run.data.tags.get('mlflow.runName', '')
    else:
        raise Exception(f'unknown text_type : {text_type}')

    return merge_html(template_name='text_editor.html',
                      params={'text_type': text_type,
                              'entity_id': entity_id,
                              'text_value': text_value,
                              },
                      display_id=display_id)


@notebook_api
def update_run_name(run_id: str, name_value: str,
                    restricted: bool = False,
                    display_id: str = None
                    ):
    _client.set_tag(run_id=run_id,
                    key='mlflow.runName',
                    value=name_value)
    return _disp_run(run_id, restricted=restricted, display_id=display_id)
