from typing import Any, Dict, Optional

import click
import yaspin

from grid import rich_click
from grid.core import Experiment, Run


def _format_log_lines(source: str, line: Dict[str, Any]) -> str:
    """Formats a log line for the terminal"""
    # If no timestamps are returned, fill the field
    # with dashes.
    log_type = click.style(source, fg="magenta")
    if not line['timestamp']:
        # Timestamps have 32 characters.
        timestamp = click.style('-' * 32, fg='green')
    else:
        timestamp = click.style(line['timestamp'], fg='green')

    return f"[{log_type}] [{timestamp}] {line['message']}"


@rich_click.command()
@rich_click.argument('experiment', type=str, nargs=1)
@click.option('--page', type=int, help='Which page to fetch from archived logs')
def logs(experiment: str, page: Optional[int]) -> None:
    """Gets logs from an Experiment."""
    spinner = yaspin.yaspin(text="Fetching logs ...", color="yellow")
    spinner.start()

    try:
        # get experiment with all its metadata
        experiment = Experiment(experiment)
        experiment.refresh()

        # get run object so we can stream image build logs
        run = Run(experiment.run["name"])

        spinner.text = "Retrieving build logs ..."

        # print run task logs
        for line in run.task_logs():
            spinner.stop()
            click.echo(_format_log_lines("build", line), nl=False)

        spinner.text = "Retrieving stdout logs ..."
        if experiment.is_queued:
            spinner.stop()

            styled_status = click.style(experiment.status, fg="blue")
            click.echo(f"Experiment is {styled_status}. Logs will be available when experiment starts.")
            return

        # print stdout logs
        # TODO: allow for other pages to be fetched from the archives
        for line in experiment.logs():
            spinner.stop()
            click.echo(_format_log_lines("stdout", line), nl=False)

    finally:
        spinner.stop()
