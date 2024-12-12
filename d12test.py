from unittest import TestCase

from d12p1 import d12p1
from d12p1 import readDataFile as readP1Data
from d12p2 import d12p2
from d12p2 import readDataFile as readP2Data


class Day12_Test(TestCase):
    def test_part1_example1(self):
        data = '''AAAA
BBCD
BBCC
EEEC'''
        self.assertEqual(d12p1(data), 140)
    
    def test_part1_example2(self):
        data = '''OOOOO
OXOXO
OOOOO
OXOXO
OOOOO'''
        self.assertEqual(d12p1(data), 772)
    
    def test_part1_example3(self):
        data = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''
        self.assertEqual(d12p1(data), 1930)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d12p1(data), 1319878)
    
    def test_part2_example1(self):
        data = '''AAAA
BBCD
BBCC
EEEC'''
        self.assertEqual(d12p2(data), 80)
    
    def test_part2_example2(self):
        data = '''OOOOO
OXOXO
OOOOO
OXOXO
OOOOO'''
        self.assertEqual(d12p2(data), 436)
    
    def test_part2_example3(self):
        data = '''EEEEE
EXXXX
EEEEE
EXXXX
EEEEE'''
        self.assertEqual(d12p2(data), 236)
    
    def test_part2_example4(self):
        data = '''AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA'''
        self.assertEqual(d12p2(data), 368)
    
    def test_part2_example5(self):
        data = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''
        self.assertEqual(d12p2(data), 1206)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d12p2(data), 784982)
