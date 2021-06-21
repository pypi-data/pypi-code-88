import click
from yucebio_scheduler.rpc.server import connect_server, create_server
import json

@click.group()
def cli():
    """作业调度&管理
    """
    pass


@cli.command()
@click.option('--port', '-p', help="当前服务绑定的端口号", type=int, required=True)
@click.option('--uri', '-u', help="jobstore的URI地址，如mongodb://user:pwd@host:port/database?options", required=True)
def server(port: int, uri: str):
    """启动作业调度器
    """
    create_server(port, uri)

@cli.group()
@click.option('--port', '-p', help="作业调度服务绑定的端口号", type=int, required=True)
@click.option('--id', '-i', help="作业的唯一ID，若指定, 自动替换相同ID的其他任务", default=None, type=str)
@click.option('--func', '-f', help="作业内容，格式为[模块:方法]， eg: yucebio_scheduler.jobs.example:example_job1", required=True)
@click.option('--args', '-a', help="作业所需的参数 [Mulitiple]", multiple=True, default=None)
@click.option('--kwargs', '-k', help="作业所需的键值对参数，如key=value [Mulitiple]", multiple=True, default=None)
@click.pass_context
def add(ctx: click.Context, **kw):
    """添加作业"""
    ctx.obj = {}
    for k,v in kw.items():
        if not v:
            continue
        ctx.obj[k] = v
    if kw['id']:
        ctx.obj['replace_existing'] = True

@add.command()
@click.option('--weeks', '-w', type=int, help="number of weeks to wait")
@click.option('--days', '-d', type=int, help="number of days to wait")
@click.option('--hours', '-h', type=int, help="number of hours to wait")
@click.option('--minutes', '-m', type=int, help="number of minutes to wait")
@click.option('--seconds', '-s', type=int, help="number of seconds to wait")
@click.option('--start_date', help="starting point for the interval calculation")
@click.option('--end_date', help="latest possible date/time to trigger on")
@click.option('--timezone', help="time zone to use for the date/time calculations")
@click.option('--jitter', type=int, help="delay the job execution by jitter seconds at most")
@click.pass_context
def interval(ctx: click.Context, **kw):
    """间断、循环执行的作业
    """
    job = dict(ctx.obj)
    for k,v in kw.items():
        if not v:
            continue
        job[k] = v

    for k in ['weeks', 'days', 'minutes', 'seconds']:
        if k in job:
            break
    else:
        click.secho('Error! 请配置任务执行间隔', fg='red')
        return
    job['trigger'] = 'interval'
    _submit_job(job)


@add.command()
@click.option('--year', '-y', type=int, help="4-digit year")
@click.option('--month', '-M', type=int, help="month (1-12)")
@click.option('--week', '-w', type=int, help="ISO week (1-53)")
@click.option('--day', '-d', type=int, help="day of month (1-31)")
@click.option('--day_of_week', help="number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)")
@click.option('--hour', '-h', type=int, help="hour (0-23)")
@click.option('--minute', '-m', type=int, help="minute (0-59)")
@click.option('--second', '-s', type=int, help="second (0-59)")
@click.option('--start_date', help="earliest possible date/time to trigger on (inclusive)")
@click.option('--end_date', help="latest possible date/time to trigger on (inclusive)")
@click.option('--jitter', type=int, help="delay the job execution by jitter seconds at most")
@click.pass_context
def cron(ctx: click.Context, **kw):
    """使用cron风格创建任务"""
    job = dict(ctx.obj)
    for k,v in kw.items():
        if not v:
            continue
        job[k] = v

    for k in ['year', 'month', 'day', 'hour', 'minute', 'second']:
        if k in job:
            break
    else:
        click.secho('Error! 请配置任务执行时间', fg='red')
        return
    job['trigger'] = 'cron'

    _submit_job(job)

@add.command()
@click.option('--run_date', '-d', help="the date/time to run the job at")
@click.pass_context
def date(ctx: click.Context, run_date):
    """立即或指定时间执行的单次作业"""
    job = dict(ctx.obj)
    if run_date:
        job['run_date'] = run_date
    job['trigger'] = 'date'

    _submit_job(job)

def _submit_job(job: dict):
    port = job.pop('port')
    ys = connect_server(port)
    ys.add_job(**job)


@cli.command()
@click.option('--port', '-p', help="作业调度服务绑定的端口号", type=int, required=True)
@click.option('--jobid', '-j', help="查看指定作业ID")
def jobs(port: int, jobid: str):
    """查看当前存在的所有作业"""
    ys = connect_server(port)
    jobs = []
    if jobid:
        jobs.append(ys.get_job(jobid))
    else:
        jobs = ys.get_jobs()

    print(json.dumps(jobs, indent=2, default=str))

@cli.command()
@click.option('--port', '-p', help="作业调度服务绑定的端口号", type=int, required=True)
@click.option('--jobid', '-j', help="查看指定作业ID")
@click.option('--action', '-a', type=click.Choice(['get', 'pause', 'resume', 'remove']), help="查询、暂停、重启、移除指定作业")
def manage(port: int, jobid: str, action: str):
    """管理（查看、暂停、重启、移除）已存在的作业"""
    ys = connect_server(port)
    func = getattr(ys, f'{action}_job')
    r = func(jobid)
    print(r)
