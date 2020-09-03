from cmd import Cmd
import six
import pyfiglet
import urllib3
import requests
import click

def log(string):
    print(pyfiglet.figlet_format(string))

@click.group()
def cli3():
    pass

@cli3.command()
def Reset():
    """Command on cli3"""
    click.echo("Using cli3")

@click.group()
def cli1():
    pass

@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@cli1.command()
def login(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        log("48HourProject")
        log("Welcome to CLI app!")
        click.echo('Hello %s!' % name)

@click.group()
def cli2():
    pass

@cli2.command()
def logout():
    """Command on cli2"""
    click.echo("Using cli2")

@click.group()
def cli3():
    pass

@cli3.command()
def HealthCheck():
    """Command on cli3"""
    click.echo("Using cli3")


cli = click.CommandCollection(sources=[cli1, cli2,cli3])

if __name__ == '__main__':
    cli()
