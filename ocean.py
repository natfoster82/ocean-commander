import click


@click.group()
def cli():
    pass


@cli.command()
def hello():
    click.echo('Howdy!')


@cli.command()
def goodbye():
    click.echo('See ya!')


if __name__ == '__main__':
    cli()
