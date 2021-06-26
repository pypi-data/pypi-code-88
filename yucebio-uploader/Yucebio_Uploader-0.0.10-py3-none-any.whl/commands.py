import click
import json
from yucebio_uploader import SupportedPlatformNames, create_uploader


def config(ctx: click.Context, param: click.Option, value: int = 0):
    # 按照定义顺序获取upload的backend默认值
    backend_option: click.Option = upload.params[2]

    backend = ctx.params.get('backend', backend_option.default)
    up = create_uploader(backend)

    print(json.dumps(up.config, indent=2))
    if click.confirm(f"是否更新[{backend}]集群配置内容", ):
        up.configure()
    ctx.exit()


@click.command()
@click.argument("src")
@click.argument("dest")
@click.option('--backend', '-b', help="需要上传文件的集群", type=click.Choice(SupportedPlatformNames), required=True)
# @click.option("--recursive", '-r', help="递归处理每个目录", is_flag=True, default=False)
@click.option('--config', '-c', help="查看并更新当前集群配置", is_flag=True, callback=config)
def upload(**kw):
    """上传文件到集群
    """
    up = create_uploader(kw['backend'])

    up.upload(kw['src'], kw['dest'])

