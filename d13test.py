from unittest import TestCase

from d13p1 import d13p1
from d13p1 import readDataFile as readP1Data
from d13p2 import d13p2
from d13p2 import readDataFile as readP2Data


class Day13_Test(TestCase):
    def test_part1_example(self):
        data = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''
        self.assertEqual(d13p1(data), 480)
    
    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d13p1(data), 28059)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d13p2(data), 102255878088512)
