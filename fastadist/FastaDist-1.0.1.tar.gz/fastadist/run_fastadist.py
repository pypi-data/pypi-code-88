import argparse
from fastadist.fastadist_functions import calculate_alignment_distances
import pkg_resources
import sys

class Version(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print(pkg_resources.require("fastadist")[0].version)
        sys.exit(0)

def parse_arguments():
    description = """
    A script to calculate distances by converting sequences to bit arrays. 
    Specify number of processes as -p N to speed up the calculation
    """
    # parse all arguments
    parser = argparse.ArgumentParser(description=description,formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.register('action', 'version', Version)

    parser.add_argument('-i', '--alignment_filepath', help='path to multiple sequence alignment input file', required = True)
    parser.add_argument('-t', '--tree_filepath', help='path to newick tree for distance matrix ordering')
    parser.add_argument('-o', '--output_filepath', help='path to distance matrix output file', required = True)
    parser.add_argument('-f', '--format', help='output format for distance matrix (one of tsv [default], csv and phylip', default = 'tsv')
    parser.add_argument('-p', '--parallel_processes', help='number of parallel processes to run (default 1)', default = 1, type = int)
    parser.add_argument('-v', '--version', action='version', nargs = 0, help='print out software version')


    return parser


def main():
    parser = parse_arguments()
    options = parser.parse_args()
    calculate_alignment_distances(options.alignment_filepath, options.output_filepath, options.format, options.parallel_processes, options.tree_filepath)

if __name__ == "__main__":
    main()

