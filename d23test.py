from unittest import TestCase

from d23p1 import d23p1
from d23p1 import readDataFile as readP1Data
from d23p2 import d23p2
from d23p2 import readDataFile as readP2Data


class Day23_Test(TestCase):
    def test_part1_example(self):
        data = '''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn'''
        self.assertEqual(d23p1(data), 7)

    def test_part1_solution(self):
        data = readP1Data()
        self.assertEqual(d23p1(data), 1230)

    def test_part2_example1(self):
        data = '''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn'''
        self.assertEqual(d23p2(data), 'co,de,ka,ta')

    def test_part2_solution(self):
        data = readP2Data()
        self.assertEqual(d23p2(data), 'az,cj,kp,lm,lt,nj,rf,rx,sn,ty,ui,wp,zo')
