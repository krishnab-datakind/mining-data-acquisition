# -*- coding: utf-8 -*-

"""Console script for dk_earth_engine_downloader."""

import click


@click.group()
@click.option('--date', nargs=2, type=str, help='beginning and end date range')
@click.option('--dir', type=click.Path(), help='path to target directory for images')
@click.argument('filename')
def main(args=None):
    """Console script for dk_earth_engine_downloader."""
    click.echo("Replace this message by putting your code into "
               "dk_earth_engine_downloader.cli.main")

@click.command()
@click.option('--radius', type=(int, float), help='image radius around location')
def points():
    pass

if __name__ == "__main__":
    main()
