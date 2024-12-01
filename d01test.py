from unittest import TestCase

from d01p1 import d01p1
from d01p1 import readDataFile as readP1Data
from d01p2 import d01p2
from d01p2 import readDataFile as readP2Data


class Day01_Test(TestCase):
    def test_part1_example(self):
        data = '''3   4
4   3
2   5
1   3
3   9
3   3
'''
        self.assertEqual(d01p1(data), 11)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d01p1(data), 1941353)

    def test_part2_example(self):
        data = '''3   4
4   3
2   5
1   3
3   9
3   3
'''
        self.assertEqual(d01p2(data), 31)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d01p2(data), 22539317)
