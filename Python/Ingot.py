#!/usr/bin/env python
"""Ingot."""
# -*- coding: utf-8 -*-

#    Worlia/Python/Ingot.py
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
0  : 2 ,
1  : 2 ,
2  : 2 ,
3  : 2 ,
4  : 2 ,
5  : 2 ,
6  : 2 ,
7  : 2 ,
8  : 2 ,
9  : 2 ,
10 : 2 ,
11 : 2 ,
12 : 2 ,
13 : 2 ,
14 : 2 ,
15 : 2 ,
16 : 2 ,
17 : 2 ,
18 : 2 ,
19 : 2 ,
20 : 2 ,
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
0  : ur"Tinern Ingot"     ,
1  : ur"Coppern Ingot"    ,
2  : ur"Blurn Ingot"      ,
3  : ur"Ironov Ingot"     ,
4  : ur"Mithrov Ingot"    ,
5  : ur"Castov Ingot"     ,
6  : ur"Stelov Ingot"     ,
7  : ur"Adamantite Ingot" ,
8  : ur"Runite Ingot"     ,
9  : ur"Karonite Ingot"   ,
10 : ur"Dragonite Ingot"  ,
11 : ur"Stalchum Ingot"   ,
12 : ur"Orichum Ingot"    ,
13 : ur"Huemachum Ingot"  ,
14 : ur"Malchum Ingot"    ,
15 : ur"Silvuo Ingot"     ,
16 : ur"Golduo Ingot"     ,
17 : ur"Chromuo Ingot"    ,
18 : ur"Platuo Ingot"     ,
19 : ur"Dalchag Ingot"    ,
20 : ur"Olmechag Ingot"   ,
}

discovers = {
0  : ur"Ksfoaek Ingot"          ,
1  : ur"Ueakd Ingot"            ,
2  : ur"Oeaisjdske Ingot"       ,
3  : ur"Jaeuasjdjd Ingot"       ,
4  : ur"Kiaee Ingot"            ,
5  : ur"LAiej Ingot"            ,
6  : ur"Ijajhejjakbvn Ingot"    ,
7  : ur"Olaejajj Ingot"         ,
8  : ur"Nvameolsd Ingot"        ,
9  : ur"Zjauieaoskdkjsje Ingot" ,
10 : ur"Raoel Ingot"            ,
11 : ur"Gajs Ingot"             ,
12 : ur"Wjafhsi Ingot"          ,
13 : ur"Idsiudak Ingot"         ,
14 : ur"Oelasp Ingot"           ,
15 : ur"Jdsjsjaek Ingot"        ,
16 : ur"Olaefajejlfe Ingot"     ,
17 : ur"Bajwk Ingot"            ,
18 : ur"Lkakspds Ingot"         ,
19 : ur"Sajaerk Ingot"          ,
20 : ur"Palkemjsfnh Ingot"      ,
}

plurals = {
0  : ( ur"Ingot" , ur"Ingots" ) ,
1  : ( ur"Ingot" , ur"Ingots" ) ,
2  : ( ur"Ingot" , ur"Ingots" ) ,
3  : ( ur"Ingot" , ur"Ingots" ) ,
4  : ( ur"Ingot" , ur"Ingots" ) ,
5  : ( ur"Ingot" , ur"Ingots" ) ,
6  : ( ur"Ingot" , ur"Ingots" ) ,
7  : ( ur"Ingot" , ur"Ingots" ) ,
8  : ( ur"Ingot" , ur"Ingots" ) ,
9  : ( ur"Ingot" , ur"Ingots" ) ,
10 : ( ur"Ingot" , ur"Ingots" ) ,
11 : ( ur"Ingot" , ur"Ingots" ) ,
12 : ( ur"Ingot" , ur"Ingots" ) ,
13 : ( ur"Ingot" , ur"Ingots" ) ,
14 : ( ur"Ingot" , ur"Ingots" ) ,
15 : ( ur"Ingot" , ur"Ingots" ) ,
16 : ( ur"Ingot" , ur"Ingots" ) ,
17 : ( ur"Ingot" , ur"Ingots" ) ,
18 : ( ur"Ingot" , ur"Ingots" ) ,
19 : ( ur"Ingot" , ur"Ingots" ) ,
20 : ( ur"Ingot" , ur"Ingots" ) ,
}

descriptions = {
0  : ur"Common found, light colour, low strength refined metal."         ,
1  : ur"Common found, medium colour, low strength refined metal."        ,
2  : ur"Common found, medium colour, low strength refined metal."        ,
3  : ur"Uncommon found, dark colour, medium strength refined metal."     ,
4  : ur"Uncommon found, medium colour, medium strength refined metal."   ,
5  : ur"Uncommon found, medium colour, medium strength refined metal."   ,
6  : ur"Uncommon found, medium colour, medium strength refined metal."   ,
7  : ur"Rare found, dark colour, high strength refined metal."           ,
8  : ur"Rare found, dark colour, high strength refined metal."           ,
9  : ur"Rare found, medium colour, high strength refined metal."         ,
10 : ur"Rare found, light colour, high strength refined metal."          ,
11 : ur"Rare found, light colour, extreme strength refined metal."       ,
12 : ur"Rare found, dark colour, extreme strength refined metal."        ,
13 : ur"Rare found, medium colour, extreme strength refined metal."      ,
14 : ur"Rare found, light colour, extreme strength refined metal."       ,
15 : ur"Legendary found, light colour, low strength refined metal."      ,
16 : ur"Legendary found, light colour, low strength refined metal."      ,
17 : ur"Legendary found, light colour, low strength refined metal."      ,
18 : ur"Legendary found, light colour, low strength refined metal."      ,
19 : ur"Legendary found, light colour, extreme strength refined metal."  ,
20 : ur"Legendary found, medium colour, extreme strength refined metal." ,
}

symbols = {
0  : ur'&' ,
1  : ur'&' ,
2  : ur'&' ,
3  : ur'&' ,
4  : ur'&' ,
5  : ur'&' ,
6  : ur'&' ,
7  : ur'&' ,
8  : ur'&' ,
9  : ur'&' ,
10 : ur'&' ,
11 : ur'&' ,
12 : ur'&' ,
13 : ur'&' ,
14 : ur'&' ,
15 : ur'&' ,
16 : ur'&' ,
17 : ur'&' ,
18 : ur'&' ,
19 : ur'&' ,
20 : ur'&' ,
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
0  : ( 0   , 0   , 0   , 1   , 2   , 3   , 4   ) ,
1  : ( 5   , 5   , 5   , 6   , 7   , 8   , 9   ) ,
2  : ( 10  , 10  , 10  , 11  , 12  , 13  , 14  ) ,
3  : ( 15  , 15  , 15  , 16  , 17  , 18  , 19  ) ,
4  : ( 20  , 20  , 20  , 21  , 22  , 23  , 24  ) ,
5  : ( 25  , 25  , 25  , 26  , 27  , 28  , 29  ) ,
6  : ( 30  , 30  , 30  , 31  , 32  , 33  , 34  ) ,
7  : ( 35  , 35  , 35  , 36  , 37  , 38  , 39  ) ,
8  : ( 40  , 40  , 40  , 41  , 42  , 43  , 44  ) ,
9  : ( 45  , 45  , 45  , 46  , 47  , 48  , 49  ) ,
10 : ( 50  , 50  , 50  , 51  , 52  , 53  , 54  ) ,
11 : ( 55  , 55  , 55  , 56  , 57  , 58  , 59  ) ,
12 : ( 60  , 60  , 60  , 61  , 62  , 63  , 64  ) ,
13 : ( 65  , 65  , 65  , 66  , 67  , 68  , 69  ) ,
14 : ( 70  , 70  , 70  , 71  , 72  , 73  , 74  ) ,
15 : ( 75  , 75  , 75  , 76  , 77  , 78  , 79  ) ,
16 : ( 80  , 80  , 80  , 81  , 82  , 83  , 84  ) ,
17 : ( 85  , 85  , 85  , 86  , 87  , 88  , 89  ) ,
18 : ( 90  , 90  , 90  , 91  , 92  , 93  , 94  ) ,
19 : ( 95  , 95  , 95  , 96  , 97  , 98  , 99  ) ,
20 : ( 100 , 100 , 100 , 100 , 100 , 100 , 100 ) ,
}

experiences = {
0  : ( 4   , 4   , 4   , 6    , 10   , 10   , 8    ) ,
1  : ( 20  , 20  , 20  , 30   , 50   , 50   , 40   ) ,
2  : ( 40  , 40  , 40  , 60   , 100  , 100  , 80   ) ,
3  : ( 60  , 60  , 60  , 90   , 150  , 150  , 120  ) ,
4  : ( 80  , 80  , 80  , 120  , 200  , 200  , 160  ) ,
5  : ( 100 , 100 , 100 , 150  , 250  , 250  , 200  ) ,
6  : ( 120 , 120 , 120 , 180  , 300  , 300  , 240  ) ,
7  : ( 140 , 140 , 140 , 210  , 350  , 350  , 280  ) ,
8  : ( 160 , 160 , 160 , 240  , 400  , 400  , 320  ) ,
9  : ( 180 , 180 , 180 , 270  , 450  , 450  , 360  ) ,
10 : ( 200 , 200 , 200 , 300  , 500  , 500  , 400  ) ,
11 : ( 440 , 440 , 440 , 660  , 1100 , 1100 , 880  ) ,
12 : ( 480 , 480 , 480 , 720  , 1200 , 1200 , 960  ) ,
13 : ( 520 , 520 , 520 , 780  , 1300 , 1300 , 1040 ) ,
14 : ( 560 , 560 , 560 , 840  , 1400 , 1400 , 1120 ) ,
15 : ( 600 , 600 , 600 , 900  , 1500 , 1500 , 1200 ) ,
16 : ( 640 , 640 , 640 , 960  , 1600 , 1600 , 1280 ) ,
17 : ( 680 , 680 , 680 , 1020 , 1700 , 1700 , 1360 ) ,
18 : ( 720 , 720 , 720 , 1080 , 1800 , 1800 , 1440 ) ,
19 : ( 760 , 760 , 760 , 1140 , 1900 , 1900 , 1520 ) ,
20 : ( 800 , 800 , 800 , 1200 , 2000 , 2000 , 1600 ) ,
}

items = {
0  : ( ( 6 , 0   ) , ( 6 , 1   ) , ( 6 , 2   ) , ( 6 , 3   ) , ( 6 , 4   ) , ( 6 , 5   ) , ( 6 , 6   ) ) ,
1  : ( ( 6 , 7   ) , ( 6 , 8   ) , ( 6 , 9   ) , ( 6 , 10  ) , ( 6 , 11  ) , ( 6 , 12  ) , ( 6 , 13  ) ) ,
2  : ( ( 6 , 14  ) , ( 6 , 15  ) , ( 6 , 16  ) , ( 6 , 17  ) , ( 6 , 18  ) , ( 6 , 19  ) , ( 6 , 20  ) ) ,
3  : ( ( 6 , 21  ) , ( 6 , 22  ) , ( 6 , 23  ) , ( 6 , 24  ) , ( 6 , 25  ) , ( 6 , 26  ) , ( 6 , 27  ) ) ,
4  : ( ( 6 , 28  ) , ( 6 , 29  ) , ( 6 , 30  ) , ( 6 , 31  ) , ( 6 , 32  ) , ( 6 , 33  ) , ( 6 , 34  ) ) ,
5  : ( ( 6 , 35  ) , ( 6 , 36  ) , ( 6 , 37  ) , ( 6 , 38  ) , ( 6 , 39  ) , ( 6 , 40  ) , ( 6 , 41  ) ) ,
6  : ( ( 6 , 42  ) , ( 6 , 43  ) , ( 6 , 44  ) , ( 6 , 45  ) , ( 6 , 46  ) , ( 6 , 47  ) , ( 6 , 48  ) ) ,
7  : ( ( 6 , 49  ) , ( 6 , 50  ) , ( 6 , 51  ) , ( 6 , 52  ) , ( 6 , 53  ) , ( 6 , 54  ) , ( 6 , 55  ) ) ,
8  : ( ( 6 , 56  ) , ( 6 , 57  ) , ( 6 , 58  ) , ( 6 , 59  ) , ( 6 , 60  ) , ( 6 , 61  ) , ( 6 , 62  ) ) ,
9  : ( ( 6 , 63  ) , ( 6 , 64  ) , ( 6 , 65  ) , ( 6 , 66  ) , ( 6 , 67  ) , ( 6 , 68  ) , ( 6 , 69  ) ) ,
10 : ( ( 6 , 70  ) , ( 6 , 71  ) , ( 6 , 72  ) , ( 6 , 73  ) , ( 6 , 74  ) , ( 6 , 75  ) , ( 6 , 76  ) ) ,
11 : ( ( 6 , 77  ) , ( 6 , 78  ) , ( 6 , 79  ) , ( 6 , 80  ) , ( 6 , 81  ) , ( 6 , 82  ) , ( 6 , 83  ) ) ,
12 : ( ( 6 , 84  ) , ( 6 , 85  ) , ( 6 , 86  ) , ( 6 , 87  ) , ( 6 , 88  ) , ( 6 , 89  ) , ( 6 , 90  ) ) ,
13 : ( ( 6 , 91  ) , ( 6 , 92  ) , ( 6 , 93  ) , ( 6 , 94  ) , ( 6 , 95  ) , ( 6 , 96  ) , ( 6 , 97  ) ) ,
14 : ( ( 6 , 98  ) , ( 6 , 99  ) , ( 6 , 100 ) , ( 6 , 101 ) , ( 6 , 102 ) , ( 6 , 103 ) , ( 6 , 104 ) ) ,
15 : ( ( 6 , 105 ) , ( 6 , 106 ) , ( 6 , 107 ) , ( 6 , 108 ) , ( 6 , 109 ) , ( 6 , 110 ) , ( 6 , 111 ) ) ,
16 : ( ( 6 , 112 ) , ( 6 , 113 ) , ( 6 , 114 ) , ( 6 , 115 ) , ( 6 , 116 ) , ( 6 , 117 ) , ( 6 , 118 ) ) ,
17 : ( ( 6 , 119 ) , ( 6 , 120 ) , ( 6 , 121 ) , ( 6 , 122 ) , ( 6 , 123 ) , ( 6 , 124 ) , ( 6 , 125 ) ) ,
18 : ( ( 6 , 126 ) , ( 6 , 127 ) , ( 6 , 128 ) , ( 6 , 129 ) , ( 6 , 130 ) , ( 6 , 131 ) , ( 6 , 132 ) ) ,
19 : ( ( 6 , 133 ) , ( 6 , 134 ) , ( 6 , 135 ) , ( 6 , 136 ) , ( 6 , 137 ) , ( 6 , 138 ) , ( 6 , 139 ) ) ,
20 : ( ( 6 , 140 ) , ( 6 , 141 ) , ( 6 , 142 ) , ( 6 , 143 ) , ( 6 , 144 ) , ( 6 , 145 ) , ( 6 , 146 ) ) ,
}

amounts = {
0  : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
1  : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
2  : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
3  : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
4  : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
5  : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
6  : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
7  : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
8  : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
9  : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
10 : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
11 : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
12 : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
13 : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
14 : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
15 : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
16 : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
17 : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
18 : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
19 : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
20 : ( 1 , 1 , 1 , 1 , 1 , 1 , 1 ) ,
}

needs = {
0  : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
1  : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
2  : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
3  : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
4  : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
5  : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
6  : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
7  : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
8  : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
9  : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
10 : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
11 : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
12 : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
13 : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
14 : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
15 : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
16 : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
17 : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
18 : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
19 : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
20 : 2 , 2 , 2 , 3 , 5 , 5 , 4 ,
}

tools = {
0  : 5 ,
1  : 5 ,
2  : 5 ,
3  : 5 ,
4  : 5 ,
5  : 5 ,
6  : 5 ,
7  : 5 ,
8  : 5 ,
9  : 5 ,
10 : 5 ,
11 : 5 ,
12 : 5 ,
13 : 5 ,
14 : 5 ,
15 : 5 ,
16 : 5 ,
17 : 5 ,
18 : 5 ,
19 : 5 ,
20 : 5 ,
}

rarities = {
0  : 3   ,
1  : 15  ,
2  : 30  ,
3  : 45  ,
4  : 60  ,
5  : 75  ,
6  : 90  ,
7  : 105 ,
8  : 120 ,
9  : 135 ,
10 : 150 ,
11 : 165 ,
12 : 180 ,
13 : 195 ,
14 : 210 ,
15 : 225 ,
16 : 240 ,
17 : 255 ,
18 : 270 ,
19 : 285 ,
20 : 300 ,
}

weights = {
0  : 1.00 ,
1  : 1.00 ,
2  : 1.00 ,
3  : 1.00 ,
4  : 1.00 ,
5  : 1.00 ,
6  : 1.00 ,
7  : 1.00 ,
8  : 1.00 ,
9  : 1.00 ,
10 : 1.00 ,
11 : 1.00 ,
12 : 1.00 ,
13 : 1.00 ,
14 : 1.00 ,
15 : 1.00 ,
16 : 1.00 ,
17 : 1.00 ,
18 : 1.00 ,
19 : 1.00 ,
20 : 1.00 ,
}

values = {
0  : 22        ,
1  : 55        ,
2  : 137       ,
3  : 302       ,
4  : 660       ,
5  : 1540      ,
6  : 3300      ,
7  : 7700      ,
8  : 19332     ,
9  : 45375     ,
10 : 106177    ,
11 : 242550    ,
12 : 544500    ,
13 : 1210935   ,
14 : 2666262   ,
15 : 5917780   ,
16 : 12363890  ,
17 : 26941200  ,
18 : 69278275  ,
19 : 155423482 ,
20 : 385902000 ,
}

tables = {
0  : ( grids[0]  , identities[0]  , names[0]  , discovers[0]  , plurals[0]  , descriptiona[0]  , symbols[0]  , foregrounds[0]  , backgrounds[0]  , spaces[0]  , windows[0]  , clips[0]  , levels[0]  , experiences[0]  , items[0]  , amounts[0]  , needs[0]  , tools[0]  , rarities[0]  , weights[0]  , values[0]  ) ,
1  : ( grids[1]  , identities[1]  , names[1]  , discovers[1]  , plurals[1]  , descriptiona[1]  , symbols[1]  , foregrounds[1]  , backgrounds[1]  , spaces[1]  , windows[1]  , clips[1]  , levels[1]  , experiences[1]  , items[1]  , amounts[1]  , needs[1]  , tools[1]  , rarities[1]  , weights[1]  , values[1]  ) ,
2  : ( grids[2]  , identities[2]  , names[2]  , discovers[2]  , plurals[2]  , descriptiona[2]  , symbols[2]  , foregrounds[2]  , backgrounds[2]  , spaces[2]  , windows[2]  , clips[2]  , levels[2]  , experiences[2]  , items[2]  , amounts[2]  , needs[2]  , tools[2]  , rarities[2]  , weights[2]  , values[2]  ) ,
3  : ( grids[3]  , identities[3]  , names[3]  , discovers[3]  , plurals[3]  , descriptiona[3]  , symbols[3]  , foregrounds[3]  , backgrounds[3]  , spaces[3]  , windows[3]  , clips[3]  , levels[3]  , experiences[3]  , items[3]  , amounts[3]  , needs[3]  , tools[3]  , rarities[3]  , weights[3]  , values[3]  ) ,
4  : ( grids[4]  , identities[4]  , names[4]  , discovers[4]  , plurals[4]  , descriptiona[4]  , symbols[4]  , foregrounds[4]  , backgrounds[4]  , spaces[4]  , windows[4]  , clips[4]  , levels[4]  , experiences[4]  , items[4]  , amounts[4]  , needs[4]  , tools[4]  , rarities[4]  , weights[4]  , values[4]  ) ,
5  : ( grids[5]  , identities[5]  , names[5]  , discovers[5]  , plurals[5]  , descriptiona[5]  , symbols[5]  , foregrounds[5]  , backgrounds[5]  , spaces[5]  , windows[5]  , clips[5]  , levels[5]  , experiences[5]  , items[5]  , amounts[5]  , needs[5]  , tools[5]  , rarities[5]  , weights[5]  , values[5]  ) ,
6  : ( grids[6]  , identities[6]  , names[6]  , discovers[6]  , plurals[6]  , descriptiona[6]  , symbols[6]  , foregrounds[6]  , backgrounds[6]  , spaces[6]  , windows[6]  , clips[6]  , levels[6]  , experiences[6]  , items[6]  , amounts[6]  , needs[6]  , tools[6]  , rarities[6]  , weights[6]  , values[6]  ) ,
7  : ( grids[7]  , identities[7]  , names[7]  , discovers[7]  , plurals[7]  , descriptiona[7]  , symbols[7]  , foregrounds[7]  , backgrounds[7]  , spaces[7]  , windows[7]  , clips[7]  , levels[7]  , experiences[7]  , items[7]  , amounts[7]  , needs[7]  , tools[7]  , rarities[7]  , weights[7]  , values[7]  ) ,
8  : ( grids[8]  , identities[8]  , names[8]  , discovers[8]  , plurals[8]  , descriptiona[8]  , symbols[8]  , foregrounds[8]  , backgrounds[8]  , spaces[8]  , windows[8]  , clips[8]  , levels[8]  , experiences[8]  , items[8]  , amounts[8]  , needs[8]  , tools[8]  , rarities[8]  , weights[8]  , values[8]  ) ,
9  : ( grids[9]  , identities[9]  , names[9]  , discovers[9]  , plurals[9]  , descriptiona[9]  , symbols[9]  , foregrounds[9]  , backgrounds[9]  , spaces[9]  , windows[9]  , clips[9]  , levels[9]  , experiences[9]  , items[9]  , amounts[9]  , needs[9]  , tools[9]  , rarities[9]  , weights[9]  , values[9]  ) ,
10 : ( grids[10] , identities[10] , names[10] , discovers[10] , plurals[10] , descriptiona[10] , symbols[10] , foregrounds[10] , backgrounds[10] , spaces[10] , windows[10] , clips[10] , levels[10] , experiences[10] , items[10] , amounts[10] , needs[10] , tools[10] , rarities[10] , weights[10] , values[10] ) ,
11 : ( grids[11] , identities[11] , names[11] , discovers[11] , plurals[11] , descriptiona[11] , symbols[11] , foregrounds[11] , backgrounds[11] , spaces[11] , windows[11] , clips[11] , levels[11] , experiences[11] , items[11] , amounts[11] , needs[11] , tools[11] , rarities[11] , weights[11] , values[11] ) ,
12 : ( grids[12] , identities[12] , names[12] , discovers[12] , plurals[12] , descriptiona[12] , symbols[12] , foregrounds[12] , backgrounds[12] , spaces[12] , windows[12] , clips[12] , levels[12] , experiences[12] , items[12] , amounts[12] , needs[12] , tools[12] , rarities[12] , weights[12] , values[12] ) ,
13 : ( grids[13] , identities[13] , names[13] , discovers[13] , plurals[13] , descriptiona[13] , symbols[13] , foregrounds[13] , backgrounds[13] , spaces[13] , windows[13] , clips[13] , levels[13] , experiences[13] , items[13] , amounts[13] , needs[13] , tools[13] , rarities[13] , weights[13] , values[13] ) ,
14 : ( grids[14] , identities[14] , names[14] , discovers[14] , plurals[14] , descriptiona[14] , symbols[14] , foregrounds[14] , backgrounds[14] , spaces[14] , windows[14] , clips[14] , levels[14] , experiences[14] , items[14] , amounts[14] , needs[14] , tools[14] , rarities[14] , weights[14] , values[14] ) ,
15 : ( grids[15] , identities[15] , names[15] , discovers[15] , plurals[15] , descriptiona[15] , symbols[15] , foregrounds[15] , backgrounds[15] , spaces[15] , windows[15] , clips[15] , levels[15] , experiences[15] , items[15] , amounts[15] , needs[15] , tools[15] , rarities[15] , weights[15] , values[15] ) ,
16 : ( grids[16] , identities[16] , names[16] , discovers[16] , plurals[16] , descriptiona[16] , symbols[16] , foregrounds[16] , backgrounds[16] , spaces[16] , windows[16] , clips[16] , levels[16] , experiences[16] , items[16] , amounts[16] , needs[16] , tools[16] , rarities[16] , weights[16] , values[16] ) ,
17 : ( grids[17] , identities[17] , names[17] , discovers[17] , plurals[17] , descriptiona[17] , symbols[17] , foregrounds[17] , backgrounds[17] , spaces[17] , windows[17] , clips[17] , levels[17] , experiences[17] , items[17] , amounts[17] , needs[17] , tools[17] , rarities[17] , weights[17] , values[17] ) ,
18 : ( grids[18] , identities[18] , names[18] , discovers[18] , plurals[18] , descriptiona[18] , symbols[18] , foregrounds[18] , backgrounds[18] , spaces[18] , windows[18] , clips[18] , levels[18] , experiences[18] , items[18] , amounts[18] , needs[18] , tools[18] , rarities[18] , weights[18] , values[18] ) ,
19 : ( grids[19] , identities[19] , names[19] , discovers[19] , plurals[19] , descriptiona[19] , symbols[19] , foregrounds[19] , backgrounds[19] , spaces[19] , windows[19] , clips[19] , levels[19] , experiences[19] , items[19] , amounts[19] , needs[19] , tools[19] , rarities[19] , weights[19] , values[19] ) ,
20 : ( grids[20] , identities[20] , names[20] , discovers[20] , plurals[20] , descriptiona[20] , symbols[20] , foregrounds[20] , backgrounds[20] , spaces[20] , windows[20] , clips[20] , levels[20] , experiences[20] , items[20] , amounts[20] , needs[20] , tools[20] , rarities[20] , weights[20] , values[20] ) ,
}
