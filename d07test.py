from unittest import TestCase

from d07p1 import d07p1
from d07p1 import readDataFile as readP1Data
from d07p2 import d07p2
from d07p2 import readDataFile as readP2Data


class Day07_Test(TestCase):
    def test_part1_example(self):
        data = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
        self.assertEqual(d07p1(data), 3749)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d07p1(data), 28730327770375)
    
    def test_part2_example(self):
        data = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
        self.assertEqual(d07p2(data), 11387)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d07p2(data), 424977609625985)
