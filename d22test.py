from unittest import TestCase

from d22p1 import d22p1
from d22p1 import readDataFile as readP1Data
from d22p2 import d22p2
from d22p2 import readDataFile as readP2Data


class Day20_Test(TestCase):
    def test_part1_example(self):
        data = '''1
10
100
2024'''
        self.assertEqual(d22p1(data, 2000), 37327623)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d22p1(data, 2000), 14392541715)

    def test_part2_example1(self):
        data = '''1
2
3
2024'''
        self.assertEqual(d22p2(data, 2000), 23)

    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d22p2(data, 2000), 1628)
