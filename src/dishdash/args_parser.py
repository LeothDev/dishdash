import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="dishdash CLI Recipe Manager")
    subparser = parser.add_subparsers(dest="command")

    add_parser = subparser.add_parser("add", help="Add a new recipe")
    add_parser.add_argument("title", help="Title of the recipe")

    return parser
