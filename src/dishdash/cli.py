from pyfiglet import Figlet

def print_banner():
    f = Figlet(font="cyberlarge")
    print(f.renderText("dishdash"))
    print("Your delicious CLI Recipe Manager")
    
def main():
    print_banner()
