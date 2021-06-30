import argparse
import random

from hoca.demo.LiteEdgeAutomaton import LiteEdgeAutomaton
from hoca.core.BasicPopulation import BasicPopulation
from hoca.core.automata_framework import Field

# Definition of default values
input_image_path = "input.png"
output_image_path = "output.png"
automata_count = 1000
stop_after = 1
automata_class = LiteEdgeAutomaton
population_class = BasicPopulation
random_seed = "This is the seed"

# command line arguments parsing
parser = argparse.ArgumentParser(description=f"Run a {population_class.__name__} of "
                                             f"{automata_class.__name__} automata.")
parser.add_argument("-i", "--input",
                    default=input_image_path,
                    help=f"input image path (default: {input_image_path})")
parser.add_argument("-o", "--output",
                    default=output_image_path,
                    help=f"output image path (default: {output_image_path})")
parser.add_argument("-rs", "--random_seed",
                    default=random_seed,
                    help=f"pseudo-random generator seed (default: {random_seed})")
parser.add_argument("-sa", "--stop_after", type=int,
                    default=stop_after,
                    help=f"number of generations to run (default:  {stop_after})")
parser.add_argument("-ac", "--automata_count", type=int,
                    default=automata_count,
                    help=f"number of automata (default:  {automata_count})")
parser.add_argument("-q", "--quiet", action="store_true",
                    help="there will be no output messages")
args = parser.parse_args()

input_image_path = args.input
output_image_path = args.output
stop_after = args.stop_after
automata_count = args.automata_count

if not args.quiet:
    # print some informative message
    print("Population class: ", population_class.describe(short=False))
    print("Input image path:", input_image_path)
    print("Output image path:", output_image_path)
    print("Stop after generation:", stop_after)

# Init the pseudo random generator to be able to replay the same population behaviour
# This is optional
random.seed(random_seed)

# Build field
field_dict = automata_class.build_field_dict(input_image_path)
# TODO: remove this when optimal_automata_count() will be implemented everywhere
if getattr(automata_class, "optimal_automata_count", None) is not None:
    first_field = list(field_dict.values())[0]
    automata_count = int(automata_class.optimal_automata_count() * first_field.width * first_field.height)

# Create the automata population and play it
automata_population = population_class(field_dict, automata_count, automata_class,
                                       stop_after=stop_after, auto_respawn=False)
automata_population.play(stop_after=stop_after)

# Save the field that may have been modified (Field.IOMode.OUT and Field.IOMode.INOUT)
for k, subfield in field_dict.items():
    if subfield.io_mode != Field.IOMode.IN:
        # TODO: handle the (possible) case when there are multiple output fields (use k)
        subfield.image.save(output_image_path)

if not args.quiet:
    # print a final report before leaving the function
    print(automata_population.describe(short=False))
    for k, subfield in field_dict.items():
        print(k, subfield)
