from unittest import TestCase

from d02p1 import d02p1
from d02p1 import readDataFile as readP1Data
from d02p2 import d02p2
from d02p2 import readDataFile as readP2Data


class Day02_Test(TestCase):
    def test_part1_example(self):
        data = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
        self.assertEqual(d02p1(data), 2)
    
    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d02p1(data), 326)
    
    def test_part2_example(self):
        data = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
        self.assertEqual(d02p2(data), 4)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d02p2(data), 381)
