# -*- coding: utf-8 -*-

"""Console script for dk_earth_engine_downloader."""

import click
from enum import Enum
from .imageCollections import ImageCollection
from .requestDirector import RequestDirector

@click.group()
@click.option('--date', nargs=2, type=str, help='beginning and end date range')
@click.option('--dir', type=click.Path(), help='path to target directory for images')
@click.argument('filename')
def main(args=None):
    """Console script for dk_earth_engine_downloader."""
    click.echo("Replace this message by putting your code into "
               "dk_earth_engine_downloader.cli.main")


    # TODO add the correct variable name here for var
    request = build_request(var)





@click.command()
@click.option('--radius', type=(int, float), help='image radius around location')
def points():
    pass



def build_request(builder):

    # TODO this might not work on the builder() since it is a variable. Fix later.
    # TODO need to have a
    tempRequest = builder()
    director = RequestDirector()
    director.construct(tempRequest)
    newRequest = tempRequest.request()
    return(newRequest)


def register_sat_image_collections():

    imagecollections = {'Landsat8' : imageCollection('LANDSAT/LC08/C01/T1',
                                                      ['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','BQA'],
                                                      '04/13/2011',
                                                      '10/07/2017'),
                        'Landsat7' : ImageCollection('LANDSAT/LE07/C01/T1',
                                                       ['B1','B2','B3','B4','B5','B6','B7'],
                                                      '01/01/1999',
                                                      '09/17/2017'),
                        'Landsat5' : imageCollection('LANDSAT/LT05/C01/T1',
                                                      ['B1','B2','B3','B4','B5','B6','B7'],
                                                      '01/01/1984',
                                                      '05/05/2012'),
                        'Sentinel2msi' : imageCollection('COPERNICUS/S2',
                                                          ['B1','B2','B3','B4','B5','B6','B7','B8','B8A','B9','B10','B11','QA10','QA20','QA60'],
                                                          '01/23/2015',
                                                          '10/20/2017'),
                        'Sentinel2sar' : ImageCollection('COPERNICUS/S1_GRD',
                                                         ['VV', 'HH',['VV', 'VH'], ['HH','HV']],
                                                         '10/03/2014',
                                                         '10/20/2017'),
                        'ModisThermalAnomalies' : ImageCollection('MODIS/006/MOD14A1',
                                                                  ['FireMask', 'MaxFRP','sample', 'QA'],
                                                                  '02/18/2000',
                                                                  '10/23/2017')
    }

class RequestTypes(Enum):
    POINTIMAGERY = 1
    DIVAGIS = 2


if __name__ == "__main__":
    main()
