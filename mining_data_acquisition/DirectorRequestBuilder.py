
#!/usr/bin/python

"""
Director Class for the Request Builder Pattern


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

class DirectorRequestBuilder():

    def __init__(self):
        self.builder = None

    def construct(self, builder, argdict):
        self.builder = builder(args)
        self.builder.originate_request()
        self.builder.validate_request()
        self.builder.assign_data()



class ValidationLogic:

    @classmethod
    def isBuilder(value):
        if not isinstance(value, abcRequest):
            raise(NotARequest)


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NotARequest(Error):
    def __init__(self, evalue):
        print('The RequestDirector() takes a Builder class as its argument.\n ' + str(evalue))





def main():
    pass


if __name__ == "__main__":
    main()
