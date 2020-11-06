from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squared import squared
from Calculator.Sqroot import sqroot
from Statistics.Mean import mean
from Statistics.Mode import mode


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

    def mode(self, a):
        self.result = mode(a)
        return self.result
