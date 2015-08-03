#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Worlia/Python/Test.py
#    Copyright (c) 2014, 2015
#    Jeremy Aaron Flexer
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

def _slots_and_deletion_inheritence_tests():
    """Test inheritence where __slots__ and refusal of private
       attribute access is concerned."""
    class BaseClass(object):
        __slots__ = ("_test_attribute", "_other_attribute")
        def __init__(self, test_attribute, other_attribute):
            self._test_attribute = test_attribute
            self._other_attribute = other_attribute
        def test_attribute(self):
            return self._test_attribute
        def other_attribute(self):
            return self._other_attribute
    class DerivedClass(BaseClass):
        __slots__ = ("_test_attribute",)
        def __init__(self, test_attribute):
            self._test_attribute = test_attribute
    base_object = BaseClass(0, 1)
    derived_object = DerivedClass(0)
    print "_slots_and_deletion_inheritence_tests():"
    print " Should print 0: '" + str(base_object.test_attribute()) + "'."
    print " Should print 1: '" + str(base_object.other_attribute()) + "'."
    print " Should print 0: '" + str(derived_object.test_attribute()) + "'."
    try:
        print " Should not print: '" + str(derived_object.other_attribute()) + "'."
    except AttributeError:
        print " Could not access not existing _other_attribute through public method in base class."

def _super_getattribute_inheritence_tests():
    """Test inheritence where __getattribute__ and using super
       to access private attributes is concerned."""
    class BaseClass(object):
        def __init__(self, test_attribute, other_attribute):
            self._test_attribute = test_attribute
            self._other_attribute = other_attribute
        def __getattribute__(self, name):
            return super(BaseClass, self).__getattribute__(name)
        def test_attribute(self):
            return self._test_attribute
        def other_attribute(self):
            return self._other_attribute
    base_object = BaseClass(0, 1)
    print "_super_getattribute_inheritence_tests():"
    try:
        print " Should print 0: '" + str(base_object.test_attribute()) + "'."
        print " Should print 1: '" + str(base_object.other_attribute()) + "'."
    except AttributeError:
        print " Could not use the super class __getattribute__ method."
    print " Use of the super class __getattribute__ method is possible."

if __name__ == "__main__":
    _slots_and_deletion_inheritence_tests()
    _super_getattribute_inheritence_tests()
