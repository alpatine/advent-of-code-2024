from unittest import TestCase

from d11p1 import d11p1
from d11p1 import readDataFile as readP1Data
from d11p2 import d11p2
from d11p2 import readDataFile as readP2Data


class Day09_Test(TestCase):
    def test_part1_example1(self):
        self.assertEqual(d11p1('0 1 10 99 999', 1), 7)
    
    def test_part1_example2(self):
        self.assertEqual(d11p1('125 17', 6), 22)
    
    def test_part1_example3(self):
        self.assertEqual(d11p1('125 17', 25), 55312)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d11p1(data, 25), 183620)
    
    def test_part2_example1(self):
        self.assertEqual(d11p1('0 1 10 99 999', 1), 7)
    
    def test_part2_example2(self):
        self.assertEqual(d11p1('125 17', 6), 22)
    
    def test_part2_example3(self):
        self.assertEqual(d11p1('125 17', 25), 55312)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d11p2(data, 75), 220377651399268)
