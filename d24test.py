from unittest import TestCase

from d24p1 import d24p1
from d24p1 import readDataFile as readP1Data
from d24p2 import d24p2
from d24p2 import readDataFile as readP2Data


class Day24_Test(TestCase):
    def test_part1_example(self):
        data = ''''''
        self.assertEqual(d24p1(data), 0000000000000)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d24p1(data), 0000000000000)

    def test_part2_example1(self):
        data = ''''''
        self.assertEqual(d24p2(data), 0000000000000)

    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d24p2(data), 0000000000000)
