from unittest import TestCase

from d14p1 import d14p1
from d14p1 import readDataFile as readP1Data
from d14p2 import d14p2
from d14p2 import readDataFile as readP2Data


class Day14_Test(TestCase):
    def test_part1_example(self):
        data = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''
        self.assertEqual(d14p1(data, 11, 7), 12)
    
    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d14p1(data, 101, 103), 211692000)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d14p2(data, 101, 103, False), 6587)
