import os
from .metadata_handler import *
import click
from .comment_processing import *
from .csv import *

@click.group()
def cli():
    pass


@click.command()
@click.option('--input', '-i', help='Path to input folder')
@click.option('--output', '-o', help='Path to new output file')
@click.option('--config', '-c', help='Path to config file', required=False, default=
                os.path.join(os.path.dirname(__file__), 'config.yml'))
def process(input, output, config):
    input = os.path.normpath(input)
    output = os.path.normpath(output)

    metadata = get_metadata(config)

    comment_processor = CommentProcessor(metadata['CODETAGS'], metadata['IGNORE_DIRECTORIES'])

    file_names = comment_processor.get_all_filenames(input)
    filtered = comment_processor.filter_list_ending(file_names, '.py')
    files_comments = comment_processor.extract_comments(input, filtered)
    files_comments = comment_processor.filter_out_comment_starts_all(files_comments)
    files_comments = comment_processor.filter_out_non_codetag_comments_all(files_comments, metadata['CODETAGS'])
    write_csv(output, files_comments, metadata['CODETAG_TO_WORK_ITEM_TYPE'])


cli.add_command(process)


if __name__ == '__main__':
    cli()