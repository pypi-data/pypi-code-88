import click
from yucebio_notifier.backend.base import BaseNotifier
from yucebio_notifier import Notifier, SUPPORTED_BACKENDS

@click.group()
def cli():
    pass


@cli.command()
def config_dingding():
    """配置钉钉和钉钉群"""
    config = BaseNotifier.config
    ding_config: dict = config('dingding', {})

    if ding_config and not click.confirm("do you want to reset config?", default= False):
        return

    corpid = click.prompt("CORP ID", default=ding_config.get('corpid'))
    corpsecret = click.prompt("CORP SECRET", default=ding_config.get('corpsecret'))
    agent_id = click.prompt("AGENT ID", default=ding_config.get('agent_id'), type=int)

    ding_config = {"corpid": corpid, "corpsecret": corpsecret, "agent_id": agent_id}
    config.update({"dingding": ding_config})
    config.save()

@cli.command()
@click.option("--user", '-u', help="接收消息的用户或钉钉群机器人编号", required=True)
@click.option("--text", '-t', help="消息标题或单行消息内容", required=True)
@click.option('--backend', '-b', help="发消息方式", type=click.Choice(SUPPORTED_BACKENDS), required=True)
def message(user: str, text: str, backend: str):
    """发送的一句话消息"""

    try:
        notifier = Notifier(backend)
        rsp = notifier.send_message(user, text)
        print("消息发送完成", rsp)
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")
        raise e


@cli.command()
@click.option("--text", '-t', help="消息标题或单行消息内容", required=True)
@click.option("--user", '-u', help="接收消息的用户或钉钉群机器人编号", required=True)
@click.option('--backend', '-b', help="发消息方式", type=click.Choice(SUPPORTED_BACKENDS), required=True)
def markdown_example(text: str, user: str, backend: str):
    """发送一条Markdonw格式的固定内容消息"""
    from yucebio_notifier.utils.markdown import Markdown

    m = Markdown()
    m.add_header(text)  
    m.add_blank().add_ref('this is a reference info').add_blank()

    value = m.convert_link('www.baidu.com', 'baidu') + ' | ' + m.convert_link('www.google.com', 'google')
    m.add_form('links', value)

    try:
        notifier = Notifier(backend)
        notifier.send_message(user, text, markdown = str(m))
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")


if __name__ == '__main__':
    cli()

