from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squared import squared
import math


def CochranSampleSize(data, confidenceLevel, confidencelevelZscore, testVaribility):
    DataLength = len(data)
    precision = subtraction(1.00, confidenceLevel)
    # print(precision)
    zScore = confidencelevelZscore
    p = testVaribility
    q = subtraction(1.00, p)
    recommendation = division(multiplication(squared(zScore), multiplication(p, q)), squared(precision))
    cochran = division(recommendation, addition(1, (division(subtraction(recommendation, 1), DataLength))))
    cochran = math.ceil(cochran)
    return cochran

