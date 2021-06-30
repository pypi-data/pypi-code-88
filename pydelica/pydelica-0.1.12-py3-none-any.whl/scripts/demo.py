import pydelica
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("input_file")
parser.add_argument("model_name")

args = parser.parse_args()

session = pydelica.Session()
session.build_model(args.input_file, args.model_name)
session.simulate(args.model_name)
print(session.get_solutions())
