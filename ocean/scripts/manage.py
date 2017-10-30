import click
from ocean.helpers import db
import digitalocean


@click.group()
def cli():
    pass


@cli.command()
@click.argument('api_token', required=False)
def set_api_token(api_token):
    if not api_token:
        api_token = click.prompt('New API Token')
    db.set('api_token', api_token)
    
    
@cli.command()
def get_all_droplets():
    token = db.get('api_token')
    manager = digitalocean.Manager(token=token)
    click.echo(manager.get_all_droplets())


if __name__ == '__main__':
    cli()
