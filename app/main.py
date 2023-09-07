from db import Base, engine, session
from models import Member, Route, Matatu
from colorama import init, Fore, Style
import click
import re

init()

@click.group()
def my_commands():
    pass

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


def error(message):
    return f"{rd}{message}{cyan}"

def blue(message):
    return f"{bl}{message}{cyan}\n"

def green(message):
    return f"{gr}{message}{cyan}\n"

def magenta(message):
    return f"{mg}{message}{cyan}\n"

def white(message):
    return f"{wh}{message}{cyan}\n"

def yellow(message):
    return f"{yl}{message}{cyan}\n"


# VALIDATORS

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

def validate_route(ctx, param, value):
    pattern = r'^[A-Za-z]+-[A-Za-z]+$'
    if not re.match(pattern, value):
        raise click.BadParameter(error('Invalid route. e.g., NRB-Juja'))
    
    return value

def validate_price(ctx, param, value):
    pattern = r'^[1-9][0-9]*[05]$'

    if not re.match(pattern, value):
        raise click.BadParameter(error('Invalid price.'))
    
    return value

def validate_number_plate(ctx, param, value):
    pattern = r'^[K][B-F][A-Z]\s[\d]{3}[A-Z]$'

    if not re.match(pattern, value):
        raise click.BadParameter(error('Invalid plates. e.g., KDF 777A'))
    
    return value


def validate_double_int(ctx, param, value):
    pattern = r'^\d{1,2}$'

    if not re.match(pattern, value) or value == '0':
        raise click.BadParameter(error('Invalid entry.'))
    
    return value

def owner_exists(ctx, param, value):
    member = session.query(Member).filter(Member.name == value).first()
    if not member:
        raise click.BadParameter(error('The owner must be an existing member.'))
    
    return value

def route_exists(ctx, param, value):
    member = session.query(Route).filter(Route.name == value).first()
    if not member:
        raise click.BadParameter(error('The owner must be an existing member.'))
    
    return value

# LOGIC

# Add a new member to the database.
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


# Add a new route to the database.

@click.command()
@click.option('--name', prompt='Name', help="Route name", callback=validate_route)
@click.option('--price', prompt='Price', help="Route price", callback=validate_price)
def add_route(name, price):
    """Add a new route to the database."""
    new_route = Route(name=name, price=price)

    session.add(new_route)
    session.commit()

    click.echo(f"Added member with ID: {new_route.id}")


# Add a new matatu to the fleet.
@click.command()
@click.option('--owner', prompt='Owner Full Name', help='Owner name - must be an existing member', callback=owner_exists)
@click.option('--route', prompt='Route Name', help='Route name - must be an existing member', callback=route_exists)
@click.option('--driver-name', prompt='Driver Full Name', help='Driver name', callback=validate_name)
@click.option('--driver-contact', prompt="Driver's Contact", help='Phone number starting with with 254', callback=validate_phone)
@click.option('--number-plate', prompt='Number Plate', help='Matatu number plate', callback=validate_number_plate)
@click.option('--capacity', prompt='Capacity', help='Matatu capacity', callback=validate_double_int)
@click.option('--avg-rounds-pd', prompt='Average Rounds Per Day', help='Average rounds per day', callback=validate_double_int)

def add_matatu(owner, route, driver_name, driver_contact, number_plate, capacity, avg_rounds_pd):
    """Add a new matatu to the fleet. Must be owned by an existing member."""
    new_matatu = Matatu(
        number_plate=number_plate,
        capacity=capacity,
        driver_name=driver_name,
        driver_contact=driver_contact,
        avg_rounds_pd=avg_rounds_pd,
        route_id=session.query(Route).filter(Route.name == route).first().id,
        member_id=session.query(Member).filter(Member.name == owner).first().id,
    )

    session.add(new_matatu)
    session.commit()

    click.echo(f"Added matatu with ID: {new_matatu.id}")

# search members
@click.command()
@click.option('--name', prompt='Name', help='Name of the member to search for')
def find_member_by_name(name):
    """Search for a member by name."""
    member = session.query(Member).filter(Member.name == name).first()

    if member:
        click.echo(f"{member}\n")
    else:
        click.echo(error(f"No member found with the name: {name} \n"))

# search routes
@click.command()
@click.option('--name', prompt='Name', help='Name of the route to search for')
def find_route_by_name(name):
    """Search for a route by name."""
    route = session.query(Route).filter(Route.name == name).first()

    if route:
        click.echo(f"{route}\n")
    else:
        click.echo(error(f"No route found with the name: {name} \n"))



# Add commands to the group
my_commands.add_command(add_member)
my_commands.add_command(add_route)
my_commands.add_command(add_matatu)
my_commands.add_command(find_member_by_name)
my_commands.add_command(find_route_by_name)



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    my_commands()