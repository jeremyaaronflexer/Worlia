#!/usr/bin/env python
"""Vein."""
# -*- coding: utf-8 -*-

#    Worlia/Python/Vein.py
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
0  : 0 ,
1  : 0 ,
2  : 0 ,
3  : 0 ,
4  : 0 ,
5  : 0 ,
6  : 0 ,
7  : 0 ,
8  : 0 ,
9  : 0 ,
10 : 0 ,
11 : 0 ,
12 : 0 ,
13 : 0 ,
14 : 0 ,
15 : 0 ,
16 : 0 ,
17 : 0 ,
18 : 0 ,
19 : 0 ,
20 : 0 ,
}

identities = {
0  : 0 ,
1  : 1 ,
2  : 2 ,
3  : 3 ,
4  : 4 ,
5  : 5 ,
6  : 6 ,
7  : 7 ,
8  : 8 ,
9  : 9 ,
10 : 10 ,
11 : 11 ,
12 : 12 ,
13 : 13 ,
14 : 14 ,
15 : 15 ,
16 : 16 ,
17 : 17 ,
18 : 18 ,
19 : 19 ,
20 : 20 ,
}

names = {
0  : ur"Tinern Vein"     ,
1  : ur"Coppern Vein"    ,
2  : ur"Blurn Vein"      ,
3  : ur"Ironov Vein"     ,
4  : ur"Mithrov Vein"    ,
5  : ur"Castov Vein"     ,
6  : ur"Stelov Vein"     ,
7  : ur"Adamantite Vein" ,
8  : ur"Runite Vein"     ,
9  : ur"Karonite Vein"   ,
10 : ur"Dragonite Vein"  ,
11 : ur"Stalchum Vein"   ,
12 : ur"Orichum Vein"    ,
13 : ur"Huemachum Vein"  ,
14 : ur"Malchum Vein"    ,
15 : ur"Silvuo Vein"     ,
16 : ur"Golduo Vein"     ,
17 : ur"Chromuo Vein"    ,
18 : ur"Platuo Vein"     ,
19 : ur"Dalchag Vein"    ,
20 : ur"Olmechag Vein"   ,
}

discovers = {
0  : ur"Ksfoaek Vein"          ,
1  : ur"Ueakd Vein"            ,
2  : ur"Oeaisjdske Vein"       ,
3  : ur"Jaeuasjdjd Vein"       ,
4  : ur"Kiaee Vein"            ,
5  : ur"LAiej Vein"            ,
6  : ur"Ijajhejjakbvn Vein"    ,
7  : ur"Olaejajj Vein"         ,
8  : ur"Nvameolsd Vein"        ,
9  : ur"Zjauieaoskdkjsje Vein" ,
10 : ur"Raoel Vein"            ,
11 : ur"Gajs Vein"             ,
12 : ur"Wjafhsi Vein"          ,
13 : ur"Idsiudak Vein"         ,
14 : ur"Oelasp Vein"           ,
15 : ur"Jdsjsjaek Vein"        ,
16 : ur"Olaefajejlfe Vein"     ,
17 : ur"Bajwk Vein"            ,
18 : ur"Lkakspds Vein"         ,
19 : ur"Sajaerk Vein"          ,
20 : ur"Palkemjsfnh Vein"      ,
}

plurals = {
0  : ( ur"Vein" , ur"Veins" ) ,
1  : ( ur"Vein" , ur"Veins" ) ,
2  : ( ur"Vein" , ur"Veins" ) ,
3  : ( ur"Vein" , ur"Veins" ) ,
4  : ( ur"Vein" , ur"Veins" ) ,
5  : ( ur"Vein" , ur"Veins" ) ,
6  : ( ur"Vein" , ur"Veins" ) ,
7  : ( ur"Vein" , ur"Veins" ) ,
8  : ( ur"Vein" , ur"Veins" ) ,
9  : ( ur"Vein" , ur"Veins" ) ,
10 : ( ur"Vein" , ur"Veins" ) ,
11 : ( ur"Vein" , ur"Veins" ) ,
12 : ( ur"Vein" , ur"Veins" ) ,
13 : ( ur"Vein" , ur"Veins" ) ,
14 : ( ur"Vein" , ur"Veins" ) ,
15 : ( ur"Vein" , ur"Veins" ) ,
16 : ( ur"Vein" , ur"Veins" ) ,
17 : ( ur"Vein" , ur"Veins" ) ,
18 : ( ur"Vein" , ur"Veins" ) ,
19 : ( ur"Vein" , ur"Veins" ) ,
20 : ( ur"Vein" , ur"Veins" ) ,
}

descriptions = {
0  : ur"Common found, light colour, low strength raw metal."         ,
1  : ur"Common found, medium colour, low strength raw metal."        ,
2  : ur"Common found, medium colour, low strength raw metal."        ,
3  : ur"Uncommon found, dark colour, medium strength raw metal."     ,
4  : ur"Uncommon found, medium colour, medium strength raw metal."   ,
5  : ur"Uncommon found, medium colour, medium strength raw metal."   ,
6  : ur"Uncommon found, medium colour, medium strength raw metal."   ,
7  : ur"Rare found, dark colour, high strength raw metal."           ,
8  : ur"Rare found, dark colour, high strength raw metal."           ,
9  : ur"Rare found, medium colour, high strength raw metal."         ,
10 : ur"Rare found, light colour, high strength raw metal."          ,
11 : ur"Rare found, light colour, extreme strength raw metal."       ,
12 : ur"Rare found, dark colour, extreme strength raw metal."        ,
13 : ur"Rare found, medium colour, extreme strength raw metal."      ,
14 : ur"Rare found, light colour, extreme strength raw metal."       ,
15 : ur"Legendary found, light colour, low strength raw metal."      ,
16 : ur"Legendary found, light colour, low strength raw metal."      ,
17 : ur"Legendary found, light colour, low strength raw metal."      ,
18 : ur"Legendary found, light colour, low strength raw metal."      ,
19 : ur"Legendary found, light colour, extreme strength raw metal."  ,
20 : ur"Legendary found, medium colour, extreme strength raw metal." ,
}

symbols = {
0  : ur';' ,
1  : ur';' ,
2  : ur';' ,
3  : ur';' ,
4  : ur';' ,
5  : ur';' ,
6  : ur';' ,
7  : ur';' ,
8  : ur';' ,
9  : ur';' ,
10 : ur';' ,
11 : ur';' ,
12 : ur';' ,
13 : ur';' ,
14 : ur';' ,
15 : ur';' ,
16 : ur';' ,
17 : ur';' ,
18 : ur';' ,
19 : ur';' ,
20 : ur';' ,
}

foregrounds = {
0  : 1 ,
1  : 1 ,
2  : 1 ,
3  : 1 ,
4  : 1 ,
5  : 1 ,
6  : 1 ,
7  : 1 ,
8  : 1 ,
9  : 1 ,
10 : 1 ,
11 : 1 ,
12 : 1 ,
13 : 1 ,
14 : 1 ,
15 : 1 ,
16 : 1 ,
17 : 1 ,
18 : 1 ,
19 : 1 ,
20 : 1 ,
}

backgrounds = {
0  : 0 ,
1  : 0 ,
2  : 0 ,
3  : 0 ,
4  : 0 ,
5  : 0 ,
6  : 0 ,
7  : 0 ,
8  : 0 ,
9  : 0 ,
10 : 0 ,
11 : 0 ,
12 : 0 ,
13 : 0 ,
14 : 0 ,
15 : 0 ,
16 : 0 ,
17 : 0 ,
18 : 0 ,
19 : 0 ,
20 : 0 ,
}

spaces = {
0  : ( ( 0 , 0 ) , ) ,
1  : ( ( 0 , 0 ) , ) ,
2  : ( ( 0 , 0 ) , ) ,
3  : ( ( 0 , 0 ) , ) ,
4  : ( ( 0 , 0 ) , ) ,
5  : ( ( 0 , 0 ) , ) ,
6  : ( ( 0 , 0 ) , ) ,
7  : ( ( 0 , 0 ) , ) ,
8  : ( ( 0 , 0 ) , ) ,
9  : ( ( 0 , 0 ) , ) ,
10 : ( ( 0 , 0 ) , ) ,
11 : ( ( 0 , 0 ) , ) ,
12 : ( ( 0 , 0 ) , ) ,
13 : ( ( 0 , 0 ) , ) ,
14 : ( ( 0 , 0 ) , ) ,
15 : ( ( 0 , 0 ) , ) ,
16 : ( ( 0 , 0 ) , ) ,
17 : ( ( 0 , 0 ) , ) ,
18 : ( ( 0 , 0 ) , ) ,
19 : ( ( 0 , 0 ) , ) ,
20 : ( ( 0 , 0 ) , ) ,
}

windows = {
0  : False ,
1  : False ,
2  : False ,
3  : False ,
4  : False ,
5  : False ,
6  : False ,
7  : False ,
8  : False ,
9  : False ,
10 : False ,
11 : False ,
12 : False ,
13 : False ,
14 : False ,
15 : False ,
16 : False ,
17 : False ,
18 : False ,
19 : False ,
20 : False ,
}

clips = {
0  : True ,
1  : True ,
2  : True ,
3  : True ,
4  : True ,
5  : True ,
6  : True ,
7  : True ,
8  : True ,
9  : True ,
10 : True ,
11 : True ,
12 : True ,
13 : True ,
14 : True ,
15 : True ,
16 : True ,
17 : True ,
18 : True ,
19 : True ,
20 : True ,
}

levels = {
0  : 0   ,
1  : 5   ,
2  : 10  ,
3  : 15  ,
4  : 20  ,
5  : 25  ,
6  : 30  ,
7  : 35  ,
8  : 40  ,
9  : 45  ,
10 : 50  ,
11 : 55  ,
12 : 60  ,
13 : 65  ,
14 : 70  ,
15 : 75  ,
16 : 80  ,
17 : 85  ,
18 : 90  ,
19 : 95  ,
20 : 100 ,
}

experiences = {
0  : 10   ,
1  : 50   ,
2  : 100  ,
3  : 150  ,
4  : 200  ,
5  : 250  ,
6  : 300  ,
7  : 350  ,
8  : 400  ,
9  : 450  ,
10 : 500  ,
11 : 625  ,
12 : 750  ,
13 : 875  ,
14 : 1000 ,
15 : 1125 ,
16 : 1250 ,
17 : 1375 ,
18 : 1500 ,
19 : 1625 ,
20 : 1750 ,
}

items = {
0  : ( 1 , 0  ) ,
1  : ( 1 , 1  ) ,
2  : ( 1 , 2  ) ,
3  : ( 1 , 3  ) ,
4  : ( 1 , 4  ) ,
5  : ( 1 , 5  ) ,
6  : ( 1 , 6  ) ,
7  : ( 1 , 7  ) ,
8  : ( 1 , 8  ) ,
9  : ( 1 , 9  ) ,
10 : ( 1 , 10 ) ,
11 : ( 1 , 11 ) ,
12 : ( 1 , 12 ) ,
13 : ( 1 , 13 ) ,
14 : ( 1 , 14 ) ,
15 : ( 1 , 15 ) ,
16 : ( 1 , 16 ) ,
17 : ( 1 , 17 ) ,
18 : ( 1 , 18 ) ,
19 : ( 1 , 19 ) ,
20 : ( 1 , 20 ) ,
}

amounts = {
0  : ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ) ,
1  : ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ) ,
2  : ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ) ,
3  : ( 1 , 2 , 3 , 4 , 5 , 6 , 7     ) ,
4  : ( 1 , 2 , 3 , 4 , 5 , 6 , 7     ) ,
5  : ( 1 , 2 , 3 , 4 , 5 , 6 , 7     ) ,
6  : ( 1 , 2 , 3 , 4 , 5 , 6 , 7     ) ,
7  : ( 1 , 2 , 3 , 4 , 5 , 6         ) ,
8  : ( 1 , 2 , 3 , 4 , 5 , 6         ) ,
9  : ( 1 , 2 , 3 , 4 , 5 , 6         ) ,
10 : ( 1 , 2 , 3 , 4 , 5 , 6         ) ,
11 : ( 1 , 2 , 3 , 4                 ) ,
12 : ( 1 , 2 , 3 , 4                 ) ,
13 : ( 1 , 2 , 3 , 4                 ) ,
14 : ( 1 , 2 , 3 , 4                 ) ,
15 : ( 1 , 2 , 3                     ) ,
16 : ( 1 , 2 , 3                     ) ,
17 : ( 1 , 2 , 3                     ) ,
18 : ( 1 , 2 , 3                     ) ,
19 : ( 1 , 2                         ) ,
20 : ( 1 , 2                         ) ,
}

tools = {
0  : 3 ,
1  : 3 ,
2  : 3 ,
3  : 3 ,
4  : 3 ,
5  : 3 ,
6  : 3 ,
7  : 3 ,
8  : 3 ,
9  : 3 ,
10 : 3 ,
11 : 3 ,
12 : 3 ,
13 : 3 ,
14 : 3 ,
15 : 3 ,
16 : 3 ,
17 : 3 ,
18 : 3 ,
19 : 3 ,
20 : 3 ,
}

rarities = {
0  : 5   ,
1  : 25  ,
2  : 50  ,
3  : 75  ,
4  : 100 ,
5  : 125 ,
6  : 150 ,
7  : 175 ,
8  : 200 ,
9  : 225 ,
10 : 250 ,
11 : 312 ,
12 : 375 ,
13 : 437 ,
14 : 500 ,
15 : 562 ,
16 : 625 ,
17 : 687 ,
18 : 750 ,
19 : 812 ,
20 : 875 ,
}

tables = {
0  : ( grids[0]  , identities[0]  , names[0]  , discovers[0]  , plurals[0]  , descriptions[0]  , symbols[0]  , foregrounds[0]  , backgrounds[0]  , spaces[0]  , windows[0]  , clips[0]  , levels[0]  , experiences[0]  , items[0]  , amounts[0]  , tools[0]  , rarities[0]  ) ,
1  : ( grids[1]  , identities[1]  , names[1]  , discovers[1]  , plurals[1]  , descriptions[1]  , symbols[1]  , foregrounds[1]  , backgrounds[1]  , spaces[1]  , windows[1]  , clips[1]  , levels[1]  , experiences[1]  , items[1]  , amounts[1]  , tools[1]  , rarities[1]  ) ,
2  : ( grids[2]  , identities[2]  , names[2]  , discovers[2]  , plurals[2]  , descriptions[2]  , symbols[2]  , foregrounds[2]  , backgrounds[2]  , spaces[2]  , windows[2]  , clips[2]  , levels[2]  , experiences[2]  , items[2]  , amounts[2]  , tools[2]  , rarities[2]  ) ,
3  : ( grids[3]  , identities[3]  , names[3]  , discovers[3]  , plurals[3]  , descriptions[3]  , symbols[3]  , foregrounds[3]  , backgrounds[3]  , spaces[3]  , windows[3]  , clips[3]  , levels[3]  , experiences[3]  , items[3]  , amounts[3]  , tools[3]  , rarities[3]  ) ,
4  : ( grids[4]  , identities[4]  , names[4]  , discovers[4]  , plurals[4]  , descriptions[4]  , symbols[4]  , foregrounds[4]  , backgrounds[4]  , spaces[4]  , windows[4]  , clips[4]  , levels[4]  , experiences[4]  , items[4]  , amounts[4]  , tools[4]  , rarities[4]  ) ,
5  : ( grids[5]  , identities[5]  , names[5]  , discovers[5]  , plurals[5]  , descriptions[5]  , symbols[5]  , foregrounds[5]  , backgrounds[5]  , spaces[5]  , windows[5]  , clips[5]  , levels[5]  , experiences[5]  , items[5]  , amounts[5]  , tools[5]  , rarities[5]  ) ,
6  : ( grids[6]  , identities[6]  , names[6]  , discovers[6]  , plurals[6]  , descriptions[6]  , symbols[6]  , foregrounds[6]  , backgrounds[6]  , spaces[6]  , windows[6]  , clips[6]  , levels[6]  , experiences[6]  , items[6]  , amounts[6]  , tools[6]  , rarities[6]  ) ,
7  : ( grids[7]  , identities[7]  , names[7]  , discovers[7]  , plurals[7]  , descriptions[7]  , symbols[7]  , foregrounds[7]  , backgrounds[7]  , spaces[7]  , windows[7]  , clips[7]  , levels[7]  , experiences[7]  , items[7]  , amounts[7]  , tools[7]  , rarities[7]  ) ,
8  : ( grids[8]  , identities[8]  , names[8]  , discovers[8]  , plurals[8]  , descriptions[8]  , symbols[8]  , foregrounds[8]  , backgrounds[8]  , spaces[8]  , windows[8]  , clips[8]  , levels[8]  , experiences[8]  , items[8]  , amounts[8]  , tools[8]  , rarities[8]  ) ,
9  : ( grids[9]  , identities[9]  , names[9]  , discovers[9]  , plurals[9]  , descriptions[9]  , symbols[9]  , foregrounds[9]  , backgrounds[9]  , spaces[9]  , windows[9]  , clips[9]  , levels[9]  , experiences[9]  , items[9]  , amounts[9]  , tools[9]  , rarities[9]  ) ,
10 : ( grids[10] , identities[10] , names[10] , discovers[10] , plurals[10] , descriptions[10] , symbols[10] , foregrounds[10] , backgrounds[10] , spaces[10] , windows[10] , clips[10] , levels[10] , experiences[10] , items[10] , amounts[10] , tools[10] , rarities[10] ) ,
11 : ( grids[11] , identities[11] , names[11] , discovers[11] , plurals[11] , descriptions[11] , symbols[11] , foregrounds[11] , backgrounds[11] , spaces[11] , windows[11] , clips[11] , levels[11] , experiences[11] , items[11] , amounts[11] , tools[11] , rarities[11] ) ,
12 : ( grids[12] , identities[12] , names[12] , discovers[12] , plurals[12] , descriptions[12] , symbols[12] , foregrounds[12] , backgrounds[12] , spaces[12] , windows[12] , clips[12] , levels[12] , experiences[12] , items[12] , amounts[12] , tools[12] , rarities[12] ) ,
13 : ( grids[13] , identities[13] , names[13] , discovers[13] , plurals[13] , descriptions[13] , symbols[13] , foregrounds[13] , backgrounds[13] , spaces[13] , windows[13] , clips[13] , levels[13] , experiences[13] , items[13] , amounts[13] , tools[13] , rarities[13] ) ,
14 : ( grids[14] , identities[14] , names[14] , discovers[14] , plurals[14] , descriptions[14] , symbols[14] , foregrounds[14] , backgrounds[14] , spaces[14] , windows[14] , clips[14] , levels[14] , experiences[14] , items[14] , amounts[14] , tools[14] , rarities[14] ) ,
15 : ( grids[15] , identities[15] , names[15] , discovers[15] , plurals[15] , descriptions[15] , symbols[15] , foregrounds[15] , backgrounds[15] , spaces[15] , windows[15] , clips[15] , levels[15] , experiences[15] , items[15] , amounts[15] , tools[15] , rarities[15] ) ,
16 : ( grids[16] , identities[16] , names[16] , discovers[16] , plurals[16] , descriptions[16] , symbols[16] , foregrounds[16] , backgrounds[16] , spaces[16] , windows[16] , clips[16] , levels[16] , experiences[16] , items[16] , amounts[16] , tools[16] , rarities[16] ) ,
17 : ( grids[17] , identities[17] , names[17] , discovers[17] , plurals[17] , descriptions[17] , symbols[17] , foregrounds[17] , backgrounds[17] , spaces[17] , windows[17] , clips[17] , levels[17] , experiences[17] , items[17] , amounts[17] , tools[17] , rarities[17] ) ,
18 : ( grids[18] , identities[18] , names[18] , discovers[18] , plurals[18] , descriptions[18] , symbols[18] , foregrounds[18] , backgrounds[18] , spaces[18] , windows[18] , clips[18] , levels[18] , experiences[18] , items[18] , amounts[18] , tools[18] , rarities[18] ) ,
19 : ( grids[19] , identities[19] , names[19] , discovers[19] , plurals[19] , descriptions[19] , symbols[19] , foregrounds[19] , backgrounds[19] , spaces[19] , windows[19] , clips[19] , levels[19] , experiences[19] , items[19] , amounts[19] , tools[19] , rarities[19] ) ,
20 : ( grids[20] , identities[20] , names[20] , discovers[20] , plurals[20] , descriptions[20] , symbols[20] , foregrounds[20] , backgrounds[20] , spaces[20] , windows[20] , clips[20] , levels[20] , experiences[20] , items[20] , amounts[20] , tools[20] , rarities[20] ) ,
}
