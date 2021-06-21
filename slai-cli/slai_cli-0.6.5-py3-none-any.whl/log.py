import click


OUTPUT_PREFIX = "slai: "


def warn(str):
    click.echo(
        f"{click.style(OUTPUT_PREFIX, bg='black', fg='white')}{click.style(str, bg='black', fg='red')}"
    )


def info(str):
    click.echo(
        f"{click.style(OUTPUT_PREFIX, bg='black', fg='white')}{click.style(str, bg='black', fg='white')}"
    )


def action(str):
    click.echo(
        f"{click.style(OUTPUT_PREFIX, bg='black', fg='white')}{click.style(str, bg='black', fg='yellow')}"
    )


def warn_confirm(str):
    return click.confirm(
        f"{click.style(OUTPUT_PREFIX, bg='black', fg='white')}{click.style(str, bg='black', fg='red')}",
    )


def action_confirm(_str):
    return click.confirm(
        f"{click.style(OUTPUT_PREFIX, bg='black', fg='white')}{click.style(_str, bg='black', fg='yellow')}",
    )


def action_prompt(str, type, default=""):
    return click.prompt(
        f"{click.style(OUTPUT_PREFIX, bg='black', fg='white')}{click.style(str, bg='black', fg='yellow')}",
        type=type,
        show_default=True,
        default=default,
    )
