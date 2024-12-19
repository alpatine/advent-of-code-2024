from unittest import TestCase

from d19p1 import d19p1
from d19p1 import readDataFile as readP1Data
from d19p2 import d19p2
from d19p2 import readDataFile as readP2Data


class Day19_Test(TestCase):
    def test_part1_example(self):
        data = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''
        self.assertEqual(d19p1(data), 6)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d19p1(data), 287)

    def test_part2_example1(self):
        data = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''
        self.assertEqual(d19p2(data), 16)

    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d19p2(data), 571894474468161)
