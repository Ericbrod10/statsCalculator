def mean(a):
    PointsSum = 0
    for i in a:
        PointsSum = PointsSum + float(i)
    return PointsSum / len(a)
