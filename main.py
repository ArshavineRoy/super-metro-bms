from app.db import Base, engine, session
from app.models import Member, Route, Matatu
from colorama import init, Fore, Back, Style
import click

init()

rd = Fore.RED
bl = Fore.BLUE
gr = Fore.GREEN
mg = Fore.MAGENTA
cyan = Fore.CYAN
yl = Fore.YELLOW
wh = Fore.WHITE

br = Style.BRIGHT
fr = Fore.RESET

smbms= '< SUPER METRO BUS MANAGEMENT SYSTEM >'
print(cyan + br + f'\n{smbms:-^50}\n')


@click.group()
def my_commands():
    pass


# add commands to the group
my_commands.add_command()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    my_commands()