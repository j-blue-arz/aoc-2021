import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 19

def mult_iters(a, b):
    return tuple(i*j for i, j in zip(a, b))

def rotmir(vec, permi, mirror):
    return mult_iters(more.nth_permutation(vec, 3, permi), mirror)

def add(a, b):
    return tuple(bi + ai for ai, bi in zip(a, b))

def delta_iters(a, b):
    """ vec from a to b"""
    return tuple(bi - ai for ai, bi in zip(a, b))

def genrotmirs(scans, permi, mirror):
    return [rotmir(vec, permi, mirror) for vec in scans]


def matchbytranslation(beacon1, beacon2, delta):
    return delta_iters(beacon1, beacon2) == delta

def try_match(scans1, scans2):
    """ find 12 matches by translation """
    set2 = set(scans2)
    for scan1 in scans1[:-11]:
        for scan2 in scans2[:-11]:
            delta = delta_iters(scan1, scan2)
            set1 = set(add(scan, delta) for scan in scans1)
            if len(set2.intersection(set1)) >= 12:
                return True, delta
    return False, 0


def match_scanners(scanner1, scanner2):
    """ search all rotmirs of beacon1 in beacon2, find 12 matches by translation
    if matches, returns True, the delta of the scanners, the the delta, mirror-vector, and permutation index of scanner2 """
    for permi in range(6):
        for mirror in product([-1, 1],[-1, 1],[-1,1]):
            match, delta = try_match(genrotmirs(scanner1, permi, mirror), scanner2)
            if match:
                return True, delta, mirror, permi
    return False, 0, 0, 0
            

def solve1(input: str):
    blocks = input.split("\n\n")
    scanners = {ints(block.splitlines()[0])[0]: [tuple(ints(line)) for line in block.splitlines()[1:]] for block in blocks}
    num_scanners = len(blocks)
    beacons = set(scanners[0])
    correct = [0]
    scannerpos = [(0, 0, 0)]
    for j in range(1, num_scanners):
        match, delta, mirror, permi = match_scanners(scanners[j], scanners[0])
        if match:
            translatedscans = [add(mult_iters(more.nth_permutation(scan, 3, permi), mirror), delta) for scan in scanners[j]]
            beacons.update(translatedscans)
            scanners[j] = translatedscans
            correct.append(j)
            scannerpos.append(delta)
    for i in correct:
        for j in range(1, num_scanners):
            if j in correct:
                continue
            match, delta, mirror, permi = match_scanners(scanners[j], scanners[i])
            if match:
                translatedscans = [add(mult_iters(more.nth_permutation(scan, 3, permi), mirror), delta) for scan in scanners[j]]
                beacons.update(translatedscans)
                scanners[j] = translatedscans
                correct.append(j)
                scannerpos.append(delta)
    
    def mhd(pos1, pos2):
        return sum(map(abs, delta_iters(pos1, pos2)))

    print(len(beacons), max(mhd(pos1, pos2) for pos1, pos2 in permutations(scannerpos, 2)))
    

def solve2(input: str):
    lines = input.splitlines()
    batches = read_batches(input)
    result = 0

    return result

examples = [
r"""
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14

""",r"""

""",r"""

""",r"""

""",r"""

""" 
]

if __name__ == "__main__":
    with_input = True
    run_with_examples_and_input(examples, solve1, "Problem 1", with_input=with_input)
    run_with_examples_and_input(examples, solve2, "Problem 2", with_input=with_input)