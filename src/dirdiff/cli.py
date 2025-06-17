import click

from dirdiff.logic import show_diff

VERSION = "0.1.0"
path=click.Path(exists=True, dir_okay=True, )

@click.command()
@click.version_option(VERSION, message="%(version)s")
@click.argument('source', type=path)
@click.argument('dest', type=path)
def cli(source, dest):
  show_diff(source, dest)
