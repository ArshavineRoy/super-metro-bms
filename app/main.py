from db import Base, engine, session
from models import Member, Route, Matatu
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

@click.command()
@click.option('--name', prompt='Name', help="Member's full name")
@click.option('--national_id', prompt='National ID', help='National ID')
@click.option('--location', prompt='Location', help='Location')
@click.option('--phone', prompt='Phone', help='Phone number with 254 prefix')
def add_member(name, national_id, location, phone):
    """Add a new member to the database."""
    new_member = Member(name=name, national_id=national_id, location=location, phone=phone)

    session.add(new_member)
    session.commit()

    click.echo(f"Added member with ID: {new_member.id}")



# add commands to the group
my_commands.add_command(add_member)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    my_commands()