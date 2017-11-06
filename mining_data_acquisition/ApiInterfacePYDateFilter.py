#!/usr/bin/python

"""

API interface to Google Earth Engine for applying Date Filter

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

import ee

class ApiInterfaceDateFilter:

    def specific_request(self, imageryCollection, strStartDate, strEndDate):
        return ValidationLogic.validateDateRange(imageryCollection, strStartDate, strEndDate)

class ValidationLogic:

    @classmethod
    def validateDateRange(cls, collection, startdate, enddate):
        try:
            collection.filterDate(startdate, enddate)
        except e:
            raise InvalidDateRange(e)


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidDateRange(Error):
    def __init__(self, evalue):
        print('The date range provided is invalid ' + str(evalue))


class Tesits:

    defi 2 test_date_range_filter(self):
        tcase =


def main():
    pass


if __name__ == "__main__":
    main()
