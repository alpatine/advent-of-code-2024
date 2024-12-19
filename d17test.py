from unittest import TestCase

from d17p1 import d17p1
from d17p1 import readDataFile as readP1Data
from d17p2 import d17p2
from d17p2 import readDataFile as readP2Data


class Day17_Test(TestCase):
    def test_part1_example(self):
        data = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''
        self.assertEqual(d17p1(data), '4,6,3,5,6,3,5,2,1,0')

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d17p1(data), '6,5,4,7,1,6,0,3,1')

    def test_part2_example1(self):
        data = '''Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0'''
        self.assertEqual(d17p2(data), 117440)

    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d17p2(data), 106086382266778)
