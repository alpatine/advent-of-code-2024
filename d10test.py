from unittest import TestCase

from d10p1 import d10p1
from d10p1 import readDataFile as readP1Data
from d10p2 import d10p2
from d10p2 import readDataFile as readP2Data


class Day10_Test(TestCase):
    def test_part1_example(self):
        data = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
        self.assertEqual(d10p1(data), 36)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d10p1(data), 652)
    
    def test_part2_example(self):
        data = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
        self.assertEqual(d10p2(data), 81)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d10p2(data), 1432)
