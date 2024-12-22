from unittest import TestCase

from d20p1 import d20p1
from d20p1 import readDataFile as readP1Data
from d20p2 import d20p2
from d20p2 import readDataFile as readP2Data


class Day20_Test(TestCase):
    def test_part1_example(self):
        data = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''
        self.assertEqual(d20p1(data, 0), 44)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d20p1(data, 100), 1384)

    def test_part2_example1(self):
        data = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''
        self.assertEqual(d20p2(data, 50), 285)

    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d20p2(data, 100), 1008542)
