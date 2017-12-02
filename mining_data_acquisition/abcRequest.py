
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
import uuid
from ValidationLogic import ValidationLogic

class abcRequest(metaclass=abc.ABCMeta):

    def __init__(self):

        self.id = uuid.uuid4()  # unique id for request
        self.statusList = None
        self.status = 1 # request status--status codes determined in request classes
        self.urllist = []
        self.settings = None

    def get_id(self):
        return self.id

    def get_status(self):
        return self.status

    def get_urllist(self):
        return self.urllist

    def get_statusList(self):
        return self.statusList

    def add_to_urllist(self, candidate):
        self.urllist.append(ValidationLogic.isURL(candidate))

    @abc.abstractmethod
    def set_statusList(self, candidate):
        pass

    @abc.abstractmethod
    def set_status(self, candidate):
        pass

    @abc.abstractmethod
    def get_data(self):
        pass


    @abc.abstractmethod
    def set_data(self):
        pass



if __name__ == "__main__":
    print("This is an abstract base class. No functionality available here.")
