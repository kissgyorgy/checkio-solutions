import itertools


def checkio(stones):
    ''' minimal possible weight difference between stone piles '''
    differences = set()
    for permutation in itertools.permutations(stones):
        # print permutation, "--->",
        right = permutation[0]
        # print str(right) + "J",
        left = 0
        for weight in permutation[1:]:
            if left <= right:
                # print str(weight)+"B",
                left += weight
            else:
                print str(weight)+"J",
                right += weight
        # print "---> MIN =", abs(left-right)
        differences.add(abs(left - right))
        # print
    # print "DIFF:", min(differences)
    return min(differences)


if __name__ == '__main__':
    assert checkio([10, 10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5, 5, 6, 5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    print 'All is ok'
