from Statistics.StandardDev import stddev
from Statistics.Mean import mean
from Calculator.Subtraction import subtraction
from Calculator.Division import division


def zscore(a):
    zscorelist = []
    DataMean = mean(a)
    for k in a:
        zscorelist.append(round(division((subtraction(k, DataMean)), (stddev(a))), 9))
    return zscorelist


