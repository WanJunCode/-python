import bisect

def grade(score,breadpoints=[60,70,80,90],grades='FDCBA'):
    # bisect == bisect_right
    i = bisect.bisect(breadpoints,score)
    return grades[i]

print([grade(score) for score in [33,99,77,70,89,90,100]])