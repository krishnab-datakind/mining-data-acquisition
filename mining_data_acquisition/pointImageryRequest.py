
#!/usr/bin/python

"""

Concrete points request class

"""

## MIT License
##
## Copyright (c) 2017, krishna bhogaonker
## Permission is hereby granted, free of charge, to any person obtaining a ## copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

## The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


__author__ = 'krishna bhogaonker'
__copyright__ = 'copyright 2017'
__credits__ = ['krishna bhogaonker']
__license__ = "MIT"
__version__ = '0.1.0'
__maintainer__ = 'krishna bhogaonker'
__email__ = 'cyclotomiq@gmail.com'
__status__ = 'pre-alpha'

from abcRequest import abcRequest
from aenum import Enum, extend_enum
import geopandas as gpd
import ee
from ValidationLogic import ValidationLogic


ee.Initialize()

class PointImageryRequest(abcRequest):

    class Composites(Enum):
        NONE = 0
        MONTHLY = 1
        QUARTERLY = 2
        YEARLY = 3


    def __init__(self):
        self.imageryCollection = None
        self.epsg = None
        self.radius = None
        self.bands = []
        self.compositedFlag = False
        self.startdate = None
        self.enddate = None
        self.geodataframe = None
        self.pointiterator = None
        self.eeCollection = None


    def get_imageryCollection(self):
        return self.imageryCollection

    def get_epsg(self):
        return self.epsg

    def get_radius(self):
        return self.radius

    def get_bands(self):
        return self.bands

    def get_compositedFlag(self):
        return self.compositedFlag

    def get_startdate(self):
        return self.startdate

    def get_enddate(self):
        return self.enddate

    def get_current_status(self):
        return self.status

    def get_string_startdate(self):

        return self.get_startdate().strftime(DATEFMT)

    def get_string_enddate(self):

        return self.get_enddate().strftime(DATEFMT)

    def get_eeCollection(self):
        return self.eeCollection

    def get_data(self):
        return self.geodataframe

    def get_data_iterator(self):
        return self.geodataframe.iterrows()

    def get_data_iterator_namedtuple(self):
        return self.geodataframe.itertuples()

    def get_list_point_coordinates(self):

        return [[p.geometry.x, p.geometry.y] for index, p in self.get_data_iterator()]

    def set_status(self, candidate):
        self.status = ValidationLogic.isInEnum(enumeration, candidate)

    def set_data(self, candidate):

        self.geodataframe = ValidationLogic.isValidSpatialFile(candidate)
        candidate_epsg =  self.geodataframe.crs['init'].replace('epsg:', '')
        self.set_epsg(candidate_epsg)
        self.pointiterator = self.get_data_iterator()


    def set_epsg(self, candidate):
        self.epsg = ValidationLogic.isInteger(ValidationLogic.isPositive(candidate))
    def set_startdate(self, candidate):
        self.startdate = ValidationLogic.is_date_string(candidate)

    def set_enddate(self, candidate):
        self.enddate = ValidationLogic.is_date_string(candidate)

    def set_radius(self, candidate):
        self.radius = ValidationLogic.isPositive(candidate)

    def set_compositedFlag(self, candidate):
        self.compositedFlag = ValidationLogic.isInEnum(candidate)

    def set_eeCollection(self, candidate):
        self.eeCollection = ee.ImageCollection(candidate)

    def set_ee_filterDate(self, start, end):
        self.eeCollection.filterDate(start, end)

    def set_statusList(self, candidate):
        self.statusList = candidate

    def ee_clip_collection(self):
        #TODO remove this function and move to handler.
        for index, row in self.get_data_iterator():

            point =  ee.Geometry.Point([row.Geometry.y, row.Geometry.x])

            def clipper(image):
                return image.clip(point.buffer(self.radius).bounds())

            self.eeCollection.map(clipper)

    def add_band(self, candidate):
        """
        This function adds a single band at a time.
        The request handler will ensure that each band requested actually exists in the imagery collection.

        Essentially, each imagery collection contains specific bands.
        The Request object does not know which bands a particular collection contains.
        Hence a user could technically request a band that does not exist, leading to a program error.

        The design here is to allow only a handler to add bands to the request.
        The handler will have knowledge of the imagery collection as well as the candidate bands.
        Once the handler knows that a band is valid for the requested collection, the handler will pass that band to the add_band() function.

        """
        self.bands.append(ValidationLogic.isstring(candidate))

    def add_column_to_data(self, columnname):

        self.get_data()[columnname] = None



class Tests:

    test = PointImageryRequest()

    def test_set_radius(self):
        self.test.set_radius(300)
        assert self.test.get_radius() == 300

    def test_set_compositedFlag(self):
        self.test.set_compositedFlag(PointImageryRequest.Composites.MONTHLY)
        assert self.test.get_compositedFlag() == PointImageryRequest.Composites.MONTHLY

    def test_set_epsg(self):
        self.test.set_epsg(4362)
        assert self.test.get_epsg() == 4362

    def test_import_data(self):
        self.test.set_data('../tests/data/congo_mines.geojson')
        assert len(self.test.geodataframe) == 2281


if __name__ == "__main__":
    main()
