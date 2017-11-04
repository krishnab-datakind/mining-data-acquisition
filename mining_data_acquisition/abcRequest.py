
#!/usr/bin/python

"""
Abstract Base Class for Request class


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


import abc
from aenum import Enum
from urllib.parse import urlparse

class abcRequest(metaclass=abc.ABCMeta):



    class Status(Enum):
        CLOSED = 0
        OPEN = 1
        REJECTED = 2
        ERROR = 3

    def __init__(self):

        self.id = uuid.uuid5()  # unique id for request
        self.status = abcRequest.Status.open # request status--status codes determined in request classes
        self.urllist = []

    def get_id(self):
        return self.id

    def get_status(self):
        return self.status

    def get_urllist(self):
        return self.urllist


    def add_to_urllist(self, candidate):
        self.urllist.append(ValidationLogic.isURL(candidate))


    @abc.abstractmethod
    def set_status(self, candidate):
        pass

    @abc.abstractmethod
    def get_data(self):
        pass

    @abc.abstractmethod
    def get_data_iterator(self):
 	    pass

    @abc.abstractmethod
    def get_list_point_coordinates(self):
        pass

    @abc.abstractmethod
    def set_data(self):
        pass


class ValidationLogic:

    @classmethod
    def isStatus(cls, value):
        if not (value in abcRequest.Status.__members__):
            raise(NotStatusError)
        else:
            return value

    def isURL(cls, value):
        try:
            result = urlparse(value)
            if (result.scheme and result.netloc and result.path):
                return(value)
        except:
            raise(NotAURL)

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NotStatusError(Error):
    def __init__(self, evalue):
        print('The value provided for the Request status must be a valid status.\n' + str(evalue))

class NotAURL(Error):
    def __init__(self, evalue):
        print('The value provided is not a valid URL.\n' + str(evalue))




if __name__ == "__main__":
    print("This is an abstract base class. No functionality available here.")
