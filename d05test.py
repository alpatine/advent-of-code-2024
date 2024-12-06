from unittest import TestCase

from d05p1 import d05p1
from d05p1 import readDataFile as readP1Data
from d05p2 import d05p2
from d05p2 import readDataFile as readP2Data


class Day05_Test(TestCase):
    def test_part1_example(self):
        data = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
        self.assertEqual(d05p1(data), 143)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d05p1(data), 5129)
    
    def test_part2_example(self):
        data = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
        self.assertEqual(d05p2(data), 123)
    
    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d05p2(data), 4077)
