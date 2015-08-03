#!/usr/bin/env python
"""Mining."""
# -*- coding: utf-8 -*-

#    Worlia/Python/Mining.py
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

import Constant as _Constant

def directional(skill_key, direction_key):
    """
    Check if 'skill_key' is a key used for mining and then check if
    'direction_key' is a key used for directions. Return 'False' if any
    checks fail. Return the directional adder if all checks succeed.
    """
    if skill_key in _Constant.KEYS_MINING:
        if direction_key in _Constant.DIRECTIONS_UP:
             return (0, -1)
        elif direction_key in _Constant.DIRECTIONS_DOWN:
             return (0, +1)
        elif direction_key in _Constant.DIRECTIONS_LEFT:
             return (-1, 0)
        elif direction_key in _Constant.DIRECTIONS_RIGHT:
             return (+1, 0)
        else:
             return False
    else:
        return False

def positional(object_grids, player_dict, directional_result):
    """
    Iterate through 'object_grids'. If something other than 'None' is
    found at the target position then return 'True'. If only 'None' is
    found at the target position on all grids then return 'False'. The
    target position is calculated using the player's current position
    found in 'player_dict' and 'directional_result'.
    """
    for object_grid in object_grids:
        if object_grid[(player_dict["positions"]["current"]["x"] + directional_result[0], player_dict["positions"]["current"]["y"] + directional_result[1])] != None:
            return True
    return False

def restrictional(player_dict):
    return player_dict["restrictions"]["Mining"]["is"]

def requiremental(vein_tables, vein_grid, player_dict, directional_result):
    return player_dict["levels"]["Mining"]["current"] >= vein_tables[vein_grid[(player_dict["positions"]["current"][0] + directional_result[0], player_dict["positions"]["current"][1] + directional_result[1])]][_Constant.VEIN_LEVEL] and player_dict["equipment"]["tool"][0] == _Constant.PICKER

def skill(vein_tables, ore_tables, formad_tables, clump_tables, geode_tables, gem_tables, picker_tables, vein_grid, formad_grid, geode_grid, player_dict, skill_key, direction_key):
    directional_result = directional(skill_key, direction_key)
    if not directional_result:
        return False
    positional_result = positional((vein_grid, formad_grid, geode_grid), player_dict, directional_result)
    if not positional_result:
        return "You can't mine that thing."
    restrictional_result = restrictional(player_dict)
    if not restrictional_result:
        return "You can't mine that currently."
    requiremental_result = requiremental(vein_tables, vein_grid, player_dict, directional_result)
    if not requiremental_result:
        return "You can't mine that yet."
    # The use is object_tables[object_grid[object_identity]][table_position_of_attribute].
    position = (player_dict["positions"]["current"][0] + directional_result[0], player_dict["positions"]["current"][1] + directional_result[1])
    experience = vein_tables[vein_grid[position]][_Constant.VEIN_EXPERIENCE]
    item = vein_tables[vein_grid[position]][_Constant.VEIN_ITEM]
    amount = vein_tables[vein_grid[position]][_Constant.VEIN_AMOUNT]
    plural = ore_tables[item][_Constant.ORE_PLURAL]
    name = ore_tables[item][_Constant.ORE_NAME]
    sname = "Mining"
    message = "Mined the {0}. Gained {1} Mining Experience. Gained {2} {3}.".format(name, experience, amount, pname or name),
    # Change singular to plural if multiple items.
    if amount > 1:
        pname = name[:name.find(plural[0])] + plural[1]
    else:
        pname = ''
    return ((sname,), (message,), (item,), (amount,), (experience,), (_Constant.VEIN,), (position,), (None,))

tables = {
0 : directional   ,
1 : positional    ,
2 : restrictional ,
3 : requiremental ,
4 : skill         ,
}
