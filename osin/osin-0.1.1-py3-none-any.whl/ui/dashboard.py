import os, math
from operator import attrgetter

import streamlit as st
import seaborn as sns
from osin.config import ROOT_DIR, CONFIG_FILE
from osin.db import ExpResult, Job
from osin.exp_config import ExpConfig
from osin.ui.toggle_list import toggle_list
from streamlit.callbacks.callbacks import periodic


# apply general settings
st.set_page_config(layout="wide")
sns.set_theme()
containers = {'jobs': None, 'exps': []}


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def get_session():
    return {}


session = get_session()


def render_jobs(force: bool = False):
    global containers, session
    with containers['jobs']:
        should_rerun = True
        if not force and session.get('last_job', None) == Job.last_finished_job():
            should_rerun = False

        if should_rerun:
            with containers['jobs']:
                jobs = get_jobs()
                session['last_job'] = Job.last_finished_job()
                toggle_list(jobs)


def periodic_check():
    """Run periodic check to see if we need to update the data"""
    global containers, session

    # TODO: check if we have new data, then update it
    if containers['jobs'] is not None:
        render_jobs()


def get_jobs():
    global session
    ptr = Job.last_finished_job()
    start = max(ptr - 3, 0)
    end = ptr + 5
    jobs = Job.select().where((Job.id >= start) & (Job.id < end))
    jobs = sorted(list(jobs), key=attrgetter('id'), reverse=True)

    return [
        dict(id=job.id,
             name=' '.join(job.exec_run_args),
             icon={"queueing": "hourglass", "success": "circle-check", "started": "spinner",
                   "failure": "triangle-exclaimation"}[job.status],
             value=job.hostname)
        for job in jobs
    ]


# render experiments
exp_configs = ExpConfig.from_file(CONFIG_FILE)
for exp_config in exp_configs:
    st.markdown(f"# {exp_config.name}")

    report_grids = exp_config.report()
    for row in report_grids:
        col_sizes = [r['colspan'] for r in row]
        if sum(col_sizes) < 24:
            # add a padding column so that streamlit don't auto-scale the columns
            col_sizes.append(24 - sum(col_sizes))

        cols = st.beta_columns(col_sizes)
        for col, report in zip(cols, row):
            with col:
                if report['display_name']:
                    st.markdown(f"### {report['name']}")
                value = report['get_value']()
                st.write(value)

    with st.form(key='run exp'):
        # create a grid
        n_cols = 3
        n_rows = math.ceil(len(exp_config.parameters) / n_cols)
        params = list(exp_config.parameters.items())
        idx = 0
        selected_params = {}
        for i in range(n_rows):
            cols = st.beta_columns(n_cols)
            for col in cols:
                with col:
                    k, v = params[idx]
                    selected_params[k] = st.multiselect(label=k, options=v)
                    idx += 1

                    if idx >= len(params):
                        break
        run_exp = st.form_submit_button(label='Run experiment')

    if run_exp:
        missing_params = [k for k, v in selected_params.items() if len(v) == 0]
        if len(missing_params) > 0:
            st.error(f"Missing values for parameter: {missing_params}")
        else:
            jobs = exp_configs[0].trigger_runs(selected_params)
            st.write(f"Start {len(jobs)} jobs.\n")

    st.markdown(f"## Raw Data")
    containers['exps'].append(st.beta_container())
    with containers['exps'][-1]:
        st.write(ExpResult.as_dataframe(exp_config.table_name))


st.markdown(f"## Running Jobs")
containers['jobs'] = st.empty()
render_jobs(force=True)


# finally run periodic check
periodic(1.0, periodic_check)