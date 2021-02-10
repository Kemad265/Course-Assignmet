def getAverage(lst):
    total=0
    for i in lst:
        total += i
    average = total / len(lst)
    return average