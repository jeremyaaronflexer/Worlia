#!/usr/bin/env python
"""Picker."""
# -*- coding: utf-8 -*-

#    Worlia/Python/Picker.py
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
0  : -1 ,
1  : -1 ,
2  : -1 ,
3  : -1 ,
4  : -1 ,
5  : -1 ,
6  : -1 ,
7  : -1 ,
8  : -1 ,
9  : -1 ,
10 : -1 ,
11 : -1 ,
12 : -1 ,
13 : -1 ,
14 : -1 ,
15 : -1 ,
16 : -1 ,
17 : -1 ,
18 : -1 ,
19 : -1 ,
20 : -1 ,
}

identities = {
0  : 0  ,
1  : 1  ,
2  : 2  ,
3  : 3  ,
4  : 4  ,
5  : 5  ,
6  : 6  ,
7  : 7  ,
8  : 8  ,
9  : 9  ,
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
0  : ur"Broken Picker"     ,
1  : ur"Makeshift Picker"  ,
2  : ur"Decrepit Picker"   ,
3  : ur"Cracked Picker"    ,
4  : ur"Ancient Picker"    ,
5  : ur"Dusty Picker"      ,
6  : ur"Rusty Picker"      ,
7  : ur"Long Picker"       ,
8  : ur"Dull Picker"       ,
9  : ur"Old Picker"        ,
10 : ur"New Picker"        ,
11 : ur"Sturdy Picker"     ,
12 : ur"Sharp Picker"      ,
13 : ur"Curved Picker"     ,
14 : ur"Rebuilt Picker"    ,
15 : ur"Blessed Picker"    ,
16 : ur"Artisan Picker"    ,
17 : ur"Reinforced Picker" ,
18 : ur"Mythical Picker"   ,
19 : ur"Shiny Picker"      ,
20 : ur"Perfect Picker"    ,
}

discovers = {
0  : ur"Koalends Picker"    ,
1  : ur"Jdoaiejhfs Picker"  ,
2  : ur"Fjaes Picker"       ,
3  : ur"Lamdoes Picker"     ,
4  : ur"Kmafoejskfh Picker" ,
5  : ur"Koajfjns Picker"    ,
6  : ur"Njfai Picker"       ,
7  : ur"Oejaejafhw Picker"  ,
8  : ur"Woaujnvm Picker"    ,
9  : ur"Lpoaejnfmnm Picker" ,
10 : ur"Olaejha Picker"     ,
11 : ur"Vhaduueu Picker"    ,
12 : ur"Ioaeuahnhvz Picker" ,
13 : ur"Ueiuambog Picker"   ,
14 : ur"Ojashdgw Picker"    ,
15 : ur"Kmvani Picker"      ,
16 : ur"Mjaoieoolvm Picker" ,
17 : ur"Hiamvozlk Picker"   ,
18 : ur"Okasnnejji Picker"  ,
19 : ur"Kjham Picker"       ,
20 : ur"Cakejos Picker"     ,
}

plurals = {
0  : ( ur"Picker" , ur"Pickers" ) ,
1  : ( ur"Picker" , ur"Pickers" ) ,
2  : ( ur"Picker" , ur"Pickers" ) ,
3  : ( ur"Picker" , ur"Pickers" ) ,
4  : ( ur"Picker" , ur"Pickers" ) ,
5  : ( ur"Picker" , ur"Pickers" ) ,
6  : ( ur"Picker" , ur"Pickers" ) ,
7  : ( ur"Picker" , ur"Pickers" ) ,
8  : ( ur"Picker" , ur"Pickers" ) ,
9  : ( ur"Picker" , ur"Pickers" ) ,
10 : ( ur"Picker" , ur"Pickers" ) ,
11 : ( ur"Picker" , ur"Pickers" ) ,
12 : ( ur"Picker" , ur"Pickers" ) ,
13 : ( ur"Picker" , ur"Pickers" ) ,
14 : ( ur"Picker" , ur"Pickers" ) ,
15 : ( ur"Picker" , ur"Pickers" ) ,
16 : ( ur"Picker" , ur"Pickers" ) ,
17 : ( ur"Picker" , ur"Pickers" ) ,
18 : ( ur"Picker" , ur"Pickers" ) ,
19 : ( ur"Picker" , ur"Pickers" ) ,
20 : ( ur"Picker" , ur"Pickers" ) ,
}

descriptions = {
0  : ur"Low quality tool used for mining."    ,
1  : ur"Low quality tool used for mining."    ,
2  : ur"Low quality tool used for mining."    ,
3  : ur"Low quality tool used for mining."    ,
4  : ur"Low quality tool used for mining."    ,
5  : ur"Low quality tool used for mining."    ,
6  : ur"Low quality tool used for mining."    ,
7  : ur"Medium quality tool used for mining." ,
8  : ur"Medium quality tool used for mining." ,
9  : ur"Medium quality tool used for mining." ,
10 : ur"Medium quality tool used for mining." ,
11 : ur"Medium quality tool used for mining." ,
12 : ur"Medium quality tool used for mining." ,
13 : ur"Medium quality tool used for mining." ,
14 : ur"High quality tool used for mining."   ,
15 : ur"High quality tool used for mining."   ,
16 : ur"High quality tool used for mining."   ,
17 : ur"High quality tool used for mining."   ,
18 : ur"High quality tool used for mining."   ,
19 : ur"High quality tool used for mining."   ,
20 : ur"High quality tool used for mining."   ,
}

symbols = {
0  : ur'?' ,
1  : ur'?' ,
2  : ur'?' ,
3  : ur'?' ,
4  : ur'?' ,
5  : ur'?' ,
6  : ur'?' ,
7  : ur'?' ,
8  : ur'?' ,
9  : ur'?' ,
10 : ur'?' ,
11 : ur'?' ,
12 : ur'?' ,
13 : ur'?' ,
14 : ur'?' ,
15 : ur'?' ,
16 : ur'?' ,
17 : ur'?' ,
18 : ur'?' ,
19 : ur'?' ,
20 : ur'?' ,
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

clips = {
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

tables = {
0  : ( grids[0]  , identities[0]  , names[0]  , discovers[0]  , plurals[0]  , descriptions[0]  , symbols[0]  , foregrounds[0]  , backgrounds[0]  , spaces[0]  , windows[0]  , clips[0]  , levels[0]  , )
1  : ( grids[1]  , identities[1]  , names[1]  , discovers[1]  , plurals[1]  , descriptions[1]  , symbols[1]  , foregrounds[1]  , backgrounds[1]  , spaces[1]  , windows[1]  , clips[1]  , levels[1]  , )
2  : ( grids[2]  , identities[2]  , names[2]  , discovers[2]  , plurals[2]  , descriptions[2]  , symbols[2]  , foregrounds[2]  , backgrounds[2]  , spaces[2]  , windows[2]  , clips[2]  , levels[2]  , )
3  : ( grids[3]  , identities[3]  , names[3]  , discovers[3]  , plurals[3]  , descriptions[3]  , symbols[3]  , foregrounds[3]  , backgrounds[3]  , spaces[3]  , windows[3]  , clips[3]  , levels[3]  , )
4  : ( grids[4]  , identities[4]  , names[4]  , discovers[4]  , plurals[4]  , descriptions[4]  , symbols[4]  , foregrounds[4]  , backgrounds[4]  , spaces[4]  , windows[4]  , clips[4]  , levels[4]  , )
5  : ( grids[5]  , identities[5]  , names[5]  , discovers[5]  , plurals[5]  , descriptions[5]  , symbols[5]  , foregrounds[5]  , backgrounds[5]  , spaces[5]  , windows[5]  , clips[5]  , levels[5]  , )
6  : ( grids[6]  , identities[6]  , names[6]  , discovers[6]  , plurals[6]  , descriptions[6]  , symbols[6]  , foregrounds[6]  , backgrounds[6]  , spaces[6]  , windows[6]  , clips[6]  , levels[6]  , )
7  : ( grids[7]  , identities[7]  , names[7]  , discovers[7]  , plurals[7]  , descriptions[7]  , symbols[7]  , foregrounds[7]  , backgrounds[7]  , spaces[7]  , windows[7]  , clips[7]  , levels[7]  , )
8  : ( grids[8]  , identities[8]  , names[8]  , discovers[8]  , plurals[8]  , descriptions[8]  , symbols[8]  , foregrounds[8]  , backgrounds[8]  , spaces[8]  , windows[8]  , clips[8]  , levels[8]  , )
9  : ( grids[9]  , identities[9]  , names[9]  , discovers[9]  , plurals[9]  , descriptions[9]  , symbols[9]  , foregrounds[9]  , backgrounds[9]  , spaces[9]  , windows[9]  , clips[9]  , levels[9]  , )
10 : ( grids[10] , identities[10] , names[10] , discovers[10] , plurals[10] , descriptions[10] , symbols[10] , foregrounds[10] , backgrounds[10] , spaces[10] , windows[10] , clips[10] , levels[10] , )
11 : ( grids[11] , identities[11] , names[11] , discovers[11] , plurals[11] , descriptions[11] , symbols[11] , foregrounds[11] , backgrounds[11] , spaces[11] , windows[11] , clips[11] , levels[11] , )
12 : ( grids[12] , identities[12] , names[12] , discovers[12] , plurals[12] , descriptions[12] , symbols[12] , foregrounds[12] , backgrounds[12] , spaces[12] , windows[12] , clips[12] , levels[12] , )
13 : ( grids[13] , identities[13] , names[13] , discovers[13] , plurals[13] , descriptions[13] , symbols[13] , foregrounds[13] , backgrounds[13] , spaces[13] , windows[13] , clips[13] , levels[13] , )
14 : ( grids[14] , identities[14] , names[14] , discovers[14] , plurals[14] , descriptions[14] , symbols[14] , foregrounds[14] , backgrounds[14] , spaces[14] , windows[14] , clips[14] , levels[14] , )
15 : ( grids[15] , identities[15] , names[15] , discovers[15] , plurals[15] , descriptions[15] , symbols[15] , foregrounds[15] , backgrounds[15] , spaces[15] , windows[15] , clips[15] , levels[15] , )
16 : ( grids[16] , identities[16] , names[16] , discovers[16] , plurals[16] , descriptions[16] , symbols[16] , foregrounds[16] , backgrounds[16] , spaces[16] , windows[16] , clips[16] , levels[16] , )
17 : ( grids[17] , identities[17] , names[17] , discovers[17] , plurals[17] , descriptions[17] , symbols[17] , foregrounds[17] , backgrounds[17] , spaces[17] , windows[17] , clips[17] , levels[17] , )
18 : ( grids[18] , identities[18] , names[18] , discovers[18] , plurals[18] , descriptions[18] , symbols[18] , foregrounds[18] , backgrounds[18] , spaces[18] , windows[18] , clips[18] , levels[18] , )
19 : ( grids[19] , identities[19] , names[19] , discovers[19] , plurals[19] , descriptions[19] , symbols[19] , foregrounds[19] , backgrounds[19] , spaces[19] , windows[19] , clips[19] , levels[19] , )
20 : ( grids[20] , identities[20] , names[20] , discovers[20] , plurals[20] , descriptions[20] , symbols[20] , foregrounds[20] , backgrounds[20] , spaces[20] , windows[20] , clips[20] , levels[20] , )
}

_ = {
0:(?, 0, "Broken Picker", "Low quality tool used for mining.", '?', 1, True, False, 0, 0, 4.0, 7),
1:(?, 1, "Makeshift Picker", "Low quality tool used for mining.", '?', 1, True, False, 5, 1, 5.0, 14),
2:(?, 2, "Decrepit Picker", "Low quality tool used for mining.", '?', 1, True, False, 10, 2, 4.0, 28),
3:(?, 3, "Cracked Picker", "Low quality tool used for mining.", '?', 1, True, False, 15, 4, 4.0, 56),
4:(?, 4, "Ancient Picker", "Low quality tool used for mining.", '?', 1, True, False, 20, 8, 4.0, 112),
5:(?, 5, "Dusty Picker", "Low quality tool used for mining.", '?', 1, True, False, 25, 16, 4.0, 224),
6:(?, 6, "Rusty Picker", "Low quality tool used for mining.", '?', 1, True, False, 30, 32, 4.0, 448),
7:(?, 7, "Long Picker",  "Medium quality tool used for mining.", '?', 1, True, False, 35, 64, 6.0, 896),
8:(?, 8, "Dull Picker", "Medium quality tool used for mining.", '?', 1, True, False, 40, 128, 4.0, 1792),
9:(?, 9, "Old Picker", "Medium quality tool used for mining.", '?', 1, True, False, 45, 256, 4.0, 3584),
10:(?, 10, "New Picker", "Medium quality tool used for mining.", '?', 1, True, False, 50, 384, 4.0, 7168),
11:(?, 11, "Sturdy Picker", "Medium quality tool used for mining.", '?', 1, True, False, 55, 512, 4.0, 14336),
12:(?, 12, "Sharp Picker", "Medium quality tool used for mining.", '?', 1, True, False, 60, 640, 4.0, 28672),
13:(?, 13, "Curved Picker", "Medium quality tool used for mining.", '?', 1, True, False, 65, 768, 5.0, 57344),
14:(?, 14, "Rebuilt Picker", "High quality tool used for mining.", '?', 1, True, False, 70, 896, 6.0, 114688),
15:(?, 15, "Blessed Picker", "High quality tool used for mining.", '?', 1, True, False, 75, 1024, 4.0, 229376),
16:(?, 16, "Artisan Picker", "High quality tool used for mining.", '?', 1, True, False, 80, 1152, 4.0, 458752),
17:(?, 17, "Reinforced Picker", "High quality tool used for mining.", '?', 1, True, False, 85, 1280, 6.0, 917504),
18:(?, 18, "Mythical Picker", "High quality tool used for mining.", '?', 1, True, False, 90, 1408, 4.0, 1835008),
19:(?, 19, "Shiny Picker", "High quality tool used for mining.", '?', 1, True, False, 95, 1536 4.0, 3670016),
20:(?, 20, "Perfect Picker", "High quality tool used for mining.", '?', 1, True, False, 100, 1664, 4.0, 7340032),
}
