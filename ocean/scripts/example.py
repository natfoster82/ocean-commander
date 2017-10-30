import click
from ocean.helpers import db


@click.group()
def cli():
    pass


@cli.command()
def hello():
    click.echo('Howdy!')


@cli.command()
def goodbye():
    click.echo('See ya!')


@cli.command()
@click.argument('key')
def get_from_db(key):
    click.echo(db.get(key))


if __name__ == '__main__':
    cli()
