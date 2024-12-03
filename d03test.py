from unittest import TestCase

from d03p1 import d03p1
from d03p1 import readDataFile as readP1Data
from d03p2 import d03p2
from d03p2 import readDataFile as readP2Data


class Day03_Test(TestCase):
    def test_part1_example(self):
        data = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''
        self.assertEqual(d03p1(data), 161)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d03p1(data), 175015740)
    
    def test_part2_example(self):
        data = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
        self.assertEqual(d03p2(data), 48)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d03p2(data), 112272912)
