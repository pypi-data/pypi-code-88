"""Console script for mfc_scraper."""
import sys
import click

from mfc_scraper import dumper


@click.command()
@click.option("-u", "--username", required=True, help="Username of the figure owner")
@click.option("-o", "--output-folder", default="output", help="Output folder path")
@click.option("--new-only/--all", default=True, help="Specifies whether only new or all data should be fetched")
@click.option("--images/--no-images", default=True, help="Specifies whether images should be fetched")
def main(username, output_folder, new_only, images):
    dumper.dump_collection(username, output_folder, new_only, images)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
