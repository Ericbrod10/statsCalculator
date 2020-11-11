from Statistics.StandardDev import stddev
from Calculator.Sqroot import sqroot
from Calculator.Division import division
from Calculator.Multiplication import multiplication


def MarginOfError(data, confidence_Zscore):
    size = len(data)
    std = stddev(data)
    z = confidence_Zscore
    Margin = multiplication(z, division(std, sqroot(size)))
    return Margin


