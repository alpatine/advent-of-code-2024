from unittest import TestCase

from d09p1 import d09p1
from d09p1 import readDataFile as readP1Data
from d09p2 import d09p2
from d09p2 import readDataFile as readP2Data


class Day09_Test(TestCase):
    def test_part1_example(self):
        data = '''2333133121414131402'''
        self.assertEqual(d09p1(data), 1928)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d09p1(data), 6360094256423)
    
    def test_part2_example(self):
        data = '''2333133121414131402'''
        self.assertEqual(d09p2(data), 2858)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d09p2(data), 6379677752410)
