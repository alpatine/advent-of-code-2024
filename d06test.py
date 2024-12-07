from unittest import TestCase

from d06p1 import d06p1
from d06p1 import readDataFile as readP1Data
from d06p2 import d06p2
from d06p2 import readDataFile as readP2Data


class Day06_Test(TestCase):
    def test_part1_example(self):
        data = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
        self.assertEqual(d06p1(data), 41)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d06p1(data), 4826)
    
    def test_part2_example(self):
        data = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
        self.assertEqual(d06p2(data), 6)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d06p2(data), 1721)
