"""Console script for event_herald."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for event_herald."""
    click.echo("You run herald of events.")
    click.echo("Have a nice day.")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
