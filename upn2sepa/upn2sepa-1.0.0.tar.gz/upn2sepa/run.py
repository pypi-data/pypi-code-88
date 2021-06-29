from upn2sepa.convert import convert
import argparse


def run():
    parser = argparse.ArgumentParser(description="Convert UPN to SEPA QR.")
    parser.add_argument('image')

    args = parser.parse_args()

    convert(args.image)
