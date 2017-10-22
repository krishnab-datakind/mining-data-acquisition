#!/usr/bin/python

"""
This module lays out a point data class.
The class will include properties on the the latitude and longitude of the point as well as information on its:
1. bounding box coordinates
2. spatial projection encoding
3. the download url
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
__version__ = "0.1.0"
__maintainer__ = "krishna bhogaonker"
__email__ = "cyclotomiq@gmail.com"
__status__ = "pre-alpha"


class PointInformation:

    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.epsg = None
        self.bounding_box_size = None
        self.bounding_box_height = None
        self.bounding_box_width = None
        self.download_url = None
        self.satellite_source = None
        self.satellite_bands = [None]

    @ValidationLogic.isnegative
    def set_latitude(self, lat):

            if (ValidationLogic.isnegative(lat) or ValidationLogic.isnotfloat(lat)):
                self.latitude = lat

    def set_longitude(self, long):

        if ValidationLogic.isnotfloat(long):
            self.longitude = long

    def set_epsg(self, epsg):

        if (ValidationLogic.isnegative(epsg) or ValidationLogic.isnotfloat(epsg)):
            self.epsg = epsg

    def set_bounding_box_size(self, size):

        if (ValidationLogic.isnegative(size) or ValidationLogic.isnotfloat(size)):
            self.bounding_box_size = size

    def set_bounding_box_height(self, height):

        if (ValidationLogic.isnegative(height) or ValidationLogic.isnotfloat(height)):
            self.bounding_box_height = height
    def set_bounding_box_width(self, width):

        if(ValidationLogic.isnegative(width) or ValidationLogic.isnotfloat(width))
            self.bounding_box_width = width
    def set_download_url(self,url):

        if(ValidationLogic.isstring(url)):
            self.download_url = url

    def set_satellite_source(self, source):

        if(ValidationLogic.isstring(source)):
            self.satellite_source = source

    def set_satellite_bands(self, bandslist):

        if (ValidationLogic.islist(bandslist)):
            self.satellite_bands = bandslist

    def get_latitute(self):

        return self.latitude

    def get_longitude(self):

        return self.longitude

    def get_epsg(self):

        return self.epsg

    def get_bounding_box_size(self):

        return self.bounding_box_size

    def get_bounding_box_height(self):

        return self.bounding_box_height

    def get_bounding_box_width(self):

        return self.bounding_box_width

    def get_download_url(self):

        return self.download_url

    def get_satellite_source(self):

        return self.satellite_source

    def get_satellite_bands(self):

        return self.satellite_bands

class ValidationLogic:

    @classmethod
    def isnotinteger(cls, value):
        try:
            return int(value)
        except ValueError as e:
            raise IsNotInteger(e)

    @classmethod
    def isnotfloat(cls,value):
        try:
            return float(value)
        except ValueError as e:
            raise IsNotFloat(e)

    @classmethod
    def isnegative(cls, value):
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




class Error(Exception):
    """Base class for exceptions in this module."""
    pass

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

if __name__ == "__main__":
    t = PointInformation()
    t.set_latitude(-2)
    print(t.latitude)
