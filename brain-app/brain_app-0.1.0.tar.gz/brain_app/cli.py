"""Console script for brain_app."""

import fire


def help():
    print("brain_app")
    print("=" * len("brain_app"))
    print("Pass")


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
