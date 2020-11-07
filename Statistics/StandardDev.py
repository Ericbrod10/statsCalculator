from Calculator.Sqroot import sqroot
from Statistics.Variance import variance


def stddev(a):
    return sqroot(variance(a))
