from pyfiglet import Figlet
from dishdash.args_parser import get_parser
from dishdash.commands import add_recipe

def print_banner():
    f = Figlet(font="cyberlarge")
    print(f.renderText("dishdash"))
    print("Your delicious CLI Recipe Manager")
    
def main():
    # print_banner()

    parser = get_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_recipe(args.title)
    else:
        parser.print_help()
