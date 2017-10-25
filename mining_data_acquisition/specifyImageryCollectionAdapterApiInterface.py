#!/usr/bin/python

"""

Low Level class to handle implementation of the SpecifyImageryCollectionAdapter abstraction.

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

class specifyImageryCollectionAdapterApiInterface:


    def __init__(self, collectionname):
        self.collectionname = collectionname

    def specific_request(self):

        return ValidationLogic.isValidCollection(self.collectionname)


class ValidationLogic:

    @classmethod
    def isValidCollection(cls, value):
        try:
            return ee.ImageCollection(value)

        except:
            raise(InvalidCollection(value))


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidCollection(Error):
    def __init__(self, evalue):
        print('The specified imagery collection is not recognized by Earth Engine:\n' + str(evalue))


class Tests:
    ee.Initialize()
    test = specifyImageryCollectionAdapterApiInterface('LANDSAT/LC8_L1T_32DAY_TOA')

    def test_collection_valid(self):
        val = self.test.specific_request()
        assert isinstance(val, ee.imagecollection.ImageCollection)


def main():
    print("This is an adapter class.")

if __name__ == "__main__":
    main()
