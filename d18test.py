from unittest import TestCase

from d18p1 import d18p1
from d18p1 import readDataFile as readP1Data
from d18p2 import d18p2
from d18p2 import readDataFile as readP2Data


class Day18_Test(TestCase):
    def test_part1_example(self):
        data = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''
        self.assertEqual(d18p1(data, 12, 7, 7), 22)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d18p1(data, 1024, 71, 71), 364)

    def test_part2_example1(self):
        data = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''
        self.assertEqual(d18p2(data, 12, 7, 7), (6, 1))

    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d18p2(data, 1024, 71, 71), (52, 28))
