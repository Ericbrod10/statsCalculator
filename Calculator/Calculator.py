from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squared import squared
from Calculator.Sqroot import sqroot
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.StandardDev import stddev
from Statistics.ZScore import zscore
from PopulationSampling.RandomSampling import SimpleRandomSampling
from PopulationSampling.ConfidenceInterval import ConfidenceInterval
from PopulationSampling.MarginOfError import MarginOfError
from PopulationSampling.Cochran import CochranSampleSize
from PopulationSampling.FindSampeSizeOfUnknownPop import UnknownPopStdSampleSize

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = squared(a)
        return self.result

    def root(self, a):
        self.result = sqroot(a)
        return self.result

    def mean(self, a):
        self.result = mean(a)
        return self.result

    def median(self, a):
        self.result = median(a)
        return self.result

    def mode(self, a):
        self.result = mode(a)
        return self.result

    def variance(self, a):
        self.result = variance(a)
        return self.result

    def stddev(self, a):
        self.result = stddev(a)
        return self.result

    def zscore(self, a):
        self.result = zscore(a)
        return self.result

    def randSample(self, a, b):
        self.result = SimpleRandomSampling(a, b)
        return self.result

    def ConfidenceInt(self, a, b):
        self.result = ConfidenceInterval(a, b)
        return self.result

    def MarginOfError(self, a, b):
        self.result = MarginOfError(a, b)
        return self.result

    def Cochran(self, a, b, c, d):
        self.result = CochranSampleSize(a, b, c, d)
        return self.result


