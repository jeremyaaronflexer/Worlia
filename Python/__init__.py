#!/usr/bin/env python
"""Init."""
# -*- coding: utf-8 -*-

#    Worlia/Python/__init__.py
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

import Ingot   as _Ingot
import Ore     as _Ore
import Vein    as _Vein
import Formad  as _Formad
import Clump   as _Clump
import Mineral as _Mineral
import Geode   as _Geode
import Gem     as _Gem
import Jewel   as _Jewel
import Tree    as _Tree
import Lumber  as _Lumber
import Log     as _Log
import Twig    as _Twig
import Leaf    as _Leaf
import Hack    as _Hack

import Mining as _Mining

objects = {
0    : _Vein     . tables ,
1    : _Ore      . tables ,
2    : _Ingot    . tables ,
3    : _Formad   . tables ,
4    : _Clump    . tables ,
5    : _Mineral  . tables ,
6    : _Geode    . tables ,
7    : _Gem      . tables ,
8    : _Jewel    . tables ,
9    : _Tree     . tables ,
10   : _Lumber   . tables ,
11   : _Log      . tables ,
12   : _Twig     . tables ,
13   : _Leaf     . tables ,
14   : _Spot     . tables ,
15   : _Fish     . tables ,
16   : _Patch    . tables ,
17   : _Bug      . tables ,
18   : _Nest     . tables ,
19   : _Bird     . tables ,
20   : _Egg      . tables ,
21   : _Picker   . tables ,
22   : _Furnace  . tables ,
23   : _Anvil    . tables ,
1031 : _Hack     . tables ,
}

skills = {
0    : _Mining . tables ,
}

grids = {
0    : { } ,
1    : { } ,
2    : { } ,
3    : { } ,
1031 : { } ,
}

player = {
"inventory"    : {},
"maps"         : {"current":None,"last":None,"history":[]},
"positions"    : {"current":(None,None),"last":(None,None),"history":[]},
"restrictions" : {"Mining":{"is":None,"time":None}},
"equipment"    : {"feet":None,"hands":None,"shoulders":None,"head":None,"legs":None,"torso":None,"back":None,"tool":None,"left_hand":None,"right_hand":None,"rings":(),},
}

characters = {
}
