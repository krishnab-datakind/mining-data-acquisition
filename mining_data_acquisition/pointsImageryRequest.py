
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
from aenum import extend_enum


class PointImageryRequest(abcRequest):





    def __init__(self):
        self.set_status(PointImageryRequest.Status.open)
        self.imageryCollection = None
        self.epsg = None
        self.radius = None
        self.bands = []
        self.compositedFlag = False
        self.startdate = None
        self.enddate = None


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

    def set_status(self, candidate):
        self.status = ValidationLogic.isStatus(candidate)

    def add_statuses_to_request(self):
        # add additional statuses to enum if needed.

        extend_enum(PointImageryRequest.Status, 'timeout', 4 )



class ValidationLogic:

    @classmethod
    def isStatus(cls, value):
        if not (value in PointImageryRequest.Status.__members__):
            raise(NotStatusError)
        else:
            return value



class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class NotStatusError(Error):
    def __init__(self, evalue):
        print('The value provided for the Request status must be a valid status.\n' + str(evalue))

class Tests:

    test = PointImageryRequest()

    def test_get_status(self):
        assert self.test.get_status() == PointImageryRequest.Status.open

    def test_extend_status(self):
        self.test.set_status(PointImageryRequest.Status.timeout)
        assert  self.test.get_status() == PointImageryRequest.Status.timeout








if __name__ == "__main__":
    main()
