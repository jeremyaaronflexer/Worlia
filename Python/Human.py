#!/usr/bin/env python
"""Human."""
# -*- coding: utf-8 -*-

#    Worlia/Python/Human.py
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

grids = {
0 : 0 ,

class _Player(object):
    """Base class Plr._Player."""
    __slots__ = ("_group", "_identity", "_name", "_description", "_health", "_mana", "_chakra", "_stamina", "_hunger", "_thirst", "_fatigue", "_levels", "_experiences", "_messages")
    def __init__(self, group, identity, name, description, health, mana, chakra, stamina, hunger, thirst, fatigue, levels, experiences, messages):
        """Initializes private attributes."""
        self._group = group
        self._identity = identity
        self._name = name
        self._description = description
        self._health = health
        self._mana = mana
        self._chakra = chakra
        self._stamina = stamina
        self._hunger = hunger
        self._thirst = thirst
        self._fatigue = fatigue
        self._levels = levels
        self._experiences = experiences
        self._messages = messages
    def __delattr__(self, attribute):
        """Stops private attribute deletion."""
        self.log("attempted deletion of attribute '" + name + "'", "../LOG/error.log")
        raise AttributeError, "deletion of attribute '" + attribute + "'  not possible"
    def __str__(self):
        """Returns string representation of object."""
        return "<Plr._Player({0} {1} '{2}' '{3}')>".format(self.group(), self.identity(), self.name(), self.description())
    def log(self, message, destination):
        """Writes the object, time, and message to a log file."""
        local = _time.localtime()
        opened = open(destination, 'a')
        opened.write('{' + str(local[1]) + '/' + str(local[2]) + '/' + str(local[0]) + ' ' + str(local[3]) + ':' + str(local[4]) + ':' + str(local[5]) + '}' + ' ' + str(self) + ' ' + '[' + str(message) + ']\n')
        opened.close()

class _Players(object):
    """Base class Plr._Players."""
    __slots__ = ("_humans", "_maps")
    def __init__(self, humans, maps):
        """Initializes private attributes."""
        self._humans = humans
        self._maps = maps

_humans = {
0:(0, 0, "Nordic Human", "Strong, hairy, warring, humans from the northern mountains.", 15, 5, 5, 15, 0, 0, 0, {"VeinMining":1}, {"VeinMining":0}, {"VeinMining":[], "All":[]})
1:(0, 1, "Nomadic Human", "Tall, magical, traveling, humans from the eastern plains.", 10, 15, 5, 10, 0, 0, 0, {"VeinMining":1}, {"VeinMining":0}, {"VeinMining":[], "All":[]})
}

_maps = {
0:"_humans"
}

def players():
    humans = _copy.copy(_humans)
    maps = _copy.copy(_maps)
    for i in humans.keys():
        humans[i] = _Human(humans[i][0], humans[i][1], humans[i][2], humans[i][3], humans[i][4], humans[i][5], humans[i][6], humans[i][7], humans[i][8], humans[i][9], humans[i][10], humans[i][11], humans[i][12], humans[i][13])
    return _Players(humans, maps)
