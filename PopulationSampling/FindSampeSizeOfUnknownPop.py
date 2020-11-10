from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squared import squared
import math


def unknown_pop_stand_deviation(data, confidenceInterval, marginOfError, percentSample):
    z = confidenceInterval
    if isinstance(marginOfError, float):
        marginOfError = marginOfError
        print(marginOfError)
    else:
        marginOfError = division(marginOfError, 100)
        # print('marginOfError:')
        # print(marginOfError)
    if isinstance(percentSample, float):
        percent = percentSample
        # print('instance Percent')
        # print(percent)
    else:
        percent = division(percentSample, 100)
        # print('else Percent')
        # print(percent)

    e = division(marginOfError, 2)
    # print('------')
    # print('e =', e)
    p = subtraction(1, percent)
    # print('p = ', p)
    SampleMultiply = multiplication(p, percent)
    # print('SampleMultiply = ', SampleMultiply)
    quotient = division(z, e)
    # print('z = ', z)
    # print('e = ', e)
    # print('z divided by e = ', quotient)
    square = squared(quotient)
    # print('square = ', square)
    result = multiplication(SampleMultiply, square)
    result = math.ceil(result)
    return result

