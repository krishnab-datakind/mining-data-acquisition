
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

from .abcRequest import abcRequest
from aenum import Enum, extend_enum
import geopandas as gpd

class PointImageryRequest(abcRequest):



    class Composites(Enum):
        NONE = 0
        MONTHLY = 1
        QUARTERLY = 2
        YEARLY = 3


    def __init__(self):
        self.set_status(abcRequest.Status.OPEN)
        self.imageryCollection = None
        self.epsg = None
        self.radius = None
        self.bands = []
        self.compositedFlag = False
        self.startdate = None
        self.enddate = None
        self.geodataframe = None
        self.add_statuses_to_request()

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

    def get_data(self):
        return self.geodataframe

    def set_status(self, candidate):
        self.status = ValidationLogic.isInEnum(candidate)

    def set_data(self, candidate):

        self.geodataframe = ValidationLogic.isValidSpatialFile(candidate)
        candidate_epsg =  self.geodataframe.crs['init'].replace('epsg:', '')
        self.set_epsg(candidate_epsg)

    def set_epsg(self, candidate):
        self.epsg = ValidationLogic.isInteger(ValidationLogic.isPositive(candidate))

    def set_startdate(self, candidate):
        self.startdate = ValidationLogic.is_date_string(candidate)

    def set_enddate(self, candidate):
        self.enddate = ValidationLogic.is_date_string(candidate)

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

    def set_radius(self, candidate):
        self.radius = ValidationLogic.isPositive(candidate)

    def set_compositedFlag(self, candidate):
        self.compositedFlag = ValidationLogic.isInEnum(candidate)

    def add_statuses_to_request(self):
        # add additional statuses to enum if needed.

        extend_enum(PointImageryRequest.Status, 'timeout', 4)



class ValidationLogic:


    @classmethod
    def isInEnum(cls, value):
        try:
            return value
        except AttributeError:
            raise(NotInEnum)

    @classmethod
    def isValidSpatialFile(cls, value):
        try:
            return(gpd.read_file(value))
        except:
            raise(NotValidSpatialFile)


    @classmethod
    def isInteger(cls, value):
        try:
            return int(value)
        except ValueError as e:
            raise IsNotInteger(e)


    @classmethod
    def isPositive(cls, value):
        if float(value) < 0:
            raise IsNegativeValue(value)
        else:
            return value


    @classmethod
    def isstring(cls, value):
        if (isinstance(value, str)):
            return value
        else:
            raise IsNotString

    @classmethod
    def islist(cls, value):

        if (isinstance(value, list)):
            return value
        else:
            raise IsNotList

    @classmethod
    def is_date_string(cls, candidate):
        try:
            return datetime.strptime(candidate, DATEFMT).date()
        except ValueError:
            raise IsNotFormattedDate

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class NotInEnum(Error):
    def __init__(self, evalue):
        print('The value entered: ' + str(evalue) + ' is not a valid member of the enum:\n')

class NotValidSpatialFile(Error):
    def __init__(self,evalue):
        print('The file provided is not a valid GeoJson or spatial file.\n' + str(evalue))

class IsNotInteger(Error):
    def __init__(self, evalue):
        print('The value entered is not an integer: ' + str(evalue))

class IsNotFloat(Error):
    def __init__(self, evalue):
        print('The value entered is not a float value: ' + str(evalue))

class IsNegativeValue(Error):
    def __init__(self, evalue):
        print('The value entered is a negative value. Negative values are not permitted for this variable: ' + str(evalue))

class IsNotString(Error):
    def __init__(self, evalue):
        print('The value entered is not a value URL: ' + str(evalue))

class IsNotList(Error):
    def __init__(self, evalue):
        print('The value entered is not a value list of values: ' + str(evalue))

class IsNotFormattedDate(Error):
    def __init__(self, evalue):
        print('The value provided is not a correctly formatted date value.\n Please provide a date in the format of mm/dd/yyyy')

class Tests:

    test = PointImageryRequest()

    def test_get_status(self):
        assert self.test.get_status() == PointImageryRequest.Status.OPEN

    def test_extend_status(self):
        self.test.set_status(PointImageryRequest.Status.timeout)
        assert  self.test.get_status() == PointImageryRequest.Status.timeout

    def test_set_radius(self):
        self.test.set_radius(300)
        assert self.test.get_radius() == 300

    def test_set_compositedFlag(self):
        self.test.set_compositedFlag(PointImageryRequest.Composites.MONTHLY)
        assert self.test.get_compositedFlag() == PointImageryRequest.Composites.MONTHLY

    def test_set_epsg(self):
        self.test.set_epsg(4362)
        assert self.test.get_epsg() == 4362




if __name__ == "__main__":
    main()
