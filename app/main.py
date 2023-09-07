from db import Base, engine, session
from models import Member, Route, Matatu
from colorama import init, Fore, Back, Style
import click
import re

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

# VALIDATORS

def error(message):
    return f"{rd}{message}{cyan}"

def validate_id(ctx, param, value):
    if not value.isdigit() or len(value) != 8:
        raise click.BadParameter(error('National ID must be 8 digits long.'))
    return value

def validate_phone(ctx, param, value):
    pattern = r'^254[71]\d{8}$'
    
    if not re.match(pattern, value):
        raise click.BadParameter(error("Invalid format. Phone numbers must start with 254."))
    
    return value

def validate_name(ctx, param, value):
    pattern = r'^[A-Za-z\s\.\'-]+ [A-Za-z\s\.\'-]+$'
    if not re.match(pattern, value):
        raise click.BadParameter(error('Invalid format. Enter full name in the correct format.'))
    
    return value

def validate_location(ctx, param, value):
    pattern = r'^[0-9A-Za-z\s\.\'-]+$'
    if not re.match(pattern, value):
        raise click.BadParameter(error('Invalid format.'))
    
    return value


# LOGIC

@click.command()
@click.option('--name', prompt='Name', help="Member's full name", callback=validate_name)
@click.option('--national_id', prompt='National ID', help='National ID', callback=validate_id)
@click.option('--location', prompt='Location', help='Location', callback=validate_location)
@click.option('--phone', prompt='Phone', help='Phone number starting with with 254', callback=validate_phone)
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