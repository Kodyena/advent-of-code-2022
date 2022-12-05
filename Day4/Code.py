is_range_inside = lambda r1, r2: (r1.start >= r2.start and r1.stop <= r2.stop) or (r2.start >= r1.start and r2.stop <= r1.stop)

do_ranges_overlap = lambda r1, r2: max(r1.start, r2.start) <= min(r1.stop, r2.stop)

with open("Day4\Data.txt") as f:
    lines = [line for line in f.read().split("\n")]
    assignments = [[[int(i) for i in assignment.split("-")] for assignment in line.split(",")] for line in lines]
    assignmentRanges = [[range(assignment[0], assignment[1]) for assignment in assignmentSet] for assignmentSet in assignments]

completelyOverlappingPairs = [rs for rs in assignmentRanges if do_ranges_overlap(rs[0], rs[1]) and is_range_inside(rs[0], rs[1])]
overlappingPairs = [rs for rs in assignmentRanges if (do_ranges_overlap(rs[0], rs[1]))]

print("Answer to Q1: {}".format(len(completelyOverlappingPairs)))
print("Answer to Q2: {}".format(len(overlappingPairs)))

