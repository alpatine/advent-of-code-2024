from unittest import TestCase

from d04p1 import d04p1
from d04p1 import readDataFile as readP1Data
from d04p2 import d04p2
from d04p2 import readDataFile as readP2Data


class Day04_Test(TestCase):
    def test_part1_example(self):
        data = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''
        self.assertEqual(d04p1(data), 18)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d04p1(data), 2496)
    
    def test_part2_example(self):
        data = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''
        self.assertEqual(d04p2(data), 9)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d04p2(data), 1967)
