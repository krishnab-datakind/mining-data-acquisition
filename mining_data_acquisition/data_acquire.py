# -*- coding: utf-8 -*-

"""Console script for dk_earth_engine_downloader."""

import click
from enum import Enum
from .imageCollection import ImageCollection
from .requestDirector import RequestDirector
from .Invoker import Invoker
from .HandlerInitializeEarthEngine import HandlerInitializeEarthEngine
from .HandlerSpecifyImageryCollection import HandlerSpecifyImageryCollection
from .CommandSimplePointImageryRequest import CommandSimplePointImageryRequest
from .HandlerSetRequestDatesFullSatelliteDateRange import HandlerSetRequestDatesFullSatelliteDateRange
from .HandlerLoadPointData import HandlerLoadPointData
from .HandlerDateFilter import HandlerDateFilter
from .HandlerPointBoundingBox import HandlerPointBoundingBox
from .HandlerPointClip import HandlerPointClip
from .HandlerPointDownloadURL import HandlerPointDownloadURL
from .HandlerURLDownloader import HandlerURLDownloader
from .BuilderPointImageryRequest import BuilderPointImageryRequest


@click.group()
@click.option('--startdate', nargs=1, type=str, help='beginning date of request')
@click.option('--enddate', nargs=1, type=str, help='end date of request')
@click.option('--dir', type=click.Path(), help='path to target directory for images')
@click.argument('filename', type=click.Path(exists=True))
def acquire_earth_engine(filename, dir, startdate, enddate):
    """Console script for dk_earth_engine_downloader."""
    click.echo("Replace this message by putting your code into "
               "acquire_earth_engine.cli.main")


    # TODO add the correct variable name here for var


    if (request_type = RequestTypes.SIMPLEPOINTIMAGERY:
        request = build_request(BuilderPointImageryRequest, locals())
        InvokerPointProcessorSimplePointImageryRequest(request)
    if (request_type = RequestTypes.COMPOSITEDPOINTIMAGERY):
        request = build_request(BuilderPointImageryRequest, locals())





@click.command()
@click.option('--radius', type=(int, float), help='image radius around location')
def points():
    pass



def build_request(builder, argdict):

    # TODO this might not work on the builder() since it is a variable. Fix later.

    tempRequest = builder(argdict)
    director = RequestDirector()
    director.construct(tempRequest)
    # TODO check if this is really tempRequest.request or tempRequest.request()

    newRequest = tempRequest.request
    return(newRequest)


def register_sat_image_collections():

    imagecollections = {'Landsat8' : imageCollection('LANDSAT/LC08/C01/T1',
                                                      ['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','BQA'],
                                                      '04/13/2011',
                                                      '10/07/2017',
                                                       30),
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


def InvokerSimplePointImageryRequest(request):

    handlers = [HandlerSetRequestDatesFullSatelliteDateRange,
                HandlerLoadPointData,
                HandlerInitializeEarthEngine,
                HandlerSpecifyImageryCollection,
                HandlerDateFilter,
                InvokerPointProcessorSimplePointImageryRequest
                ]

    invoker = Invoker()

    for c in handlers:
        invoker.store_command(c(request).handle())


    invoker.execute_commands()


def Handler

    pass



class RequestTypes(Enum):
    SIMPLEPOINTIMAGERY = 1
    DIVAGIS = 2
    COMPOSITEDPOINTIMAGERY = 3

if __name__ == "__main__":
    main()
