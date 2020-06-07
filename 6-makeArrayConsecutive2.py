def makeArrayConsecutive2(statues):
    statues.sort()
    missing_statues = 0
    for i in range(1, len(statues)):
        if statues[i] - statues[i - 1] < 2:
            continue
        else:
            missing_statues += statues[i] - statues[i - 1] - 1
    return missing_statues


print(makeArrayConsecutive2([9, 3, 5, 2]))
