import click
from oceania.main.client import get_secuences_from_fasta_to_file


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def main():
    """A simple OceanIA command line tool."""


@main.command()
@click.argument("key", required=True, metavar="<key>")
@click.argument(
    "query_file", required=True, metavar="<query_file>", type=click.File("r")
)
@click.argument("output_format", required=True, metavar="<output_format>")
@click.argument(
    "output_file", required=True, metavar="<output_file>", type=click.File("wb")
)
def query_fasta(key, query_file, output_format, output_file):
    """Extract secuences from a fasta file in the OceanIA Storage.

    \b
    <key> object key in the OceanIA storage
    <query_file> CSV file containing the values to query.
                 Each line represents a sequence to extract in the format "sequence_id,start,end,type"
                 "sequence_id" sequence ID
                 "start" start index position of the sequence to be extracted
                 "end" end index position of the sequence to extract
                 "type" type of the sequence to extract
                        options are ["raw", "complement", "reverse_complement"]
                        type value is optional, if not provided default is "raw"
    <output_format> results format
                    options are ["csv", "fasta"]
    <output_file> name of the file to write the results
    """

    query_list = []

    for row in query_file:
        raw_values = row.rstrip().split(",")
        if len(raw_values) >= 3:
            values = [raw_values[0], int(raw_values[1]), int(raw_values[2])]
        if len(raw_values) > 3:
            values.append(raw_values[3])
        query_list.append(values)

    if len(query_list) > 0:
        get_secuences_from_fasta_to_file(
            key, query_list, output_format, output_file
        )
