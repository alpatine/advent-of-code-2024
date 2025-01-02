from unittest import TestCase

from d25p1 import d25p1
from d25p1 import readDataFile as readP1Data


class Day24_Test(TestCase):
    def test_part1_example(self):
        data = '''#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####'''
        self.assertEqual(d25p1(data), 3)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d25p1(data), 2691)
