from unittest import TestCase

from d21p1 import d21p1
from d21p1 import readDataFile as readP1Data
from d21p2 import d21p2
from d21p2 import readDataFile as readP2Data


class Day20_Test(TestCase):
    def test_part1_example(self):
        data = '''029A
980A
179A
456A
379A'''
        self.assertEqual(d21p1(data), 126384)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d21p1(data), 246990)

    # def test_part2_example1(self):
    #     data = ''''''
    #     self.assertEqual(d21p2(data), 285)

    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d21p2(data, 25), 306335137543664)
