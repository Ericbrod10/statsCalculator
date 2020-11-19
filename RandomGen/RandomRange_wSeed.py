import random


def randIntwSeed(a, b, c):
    random.seed(c)
    num = random.randint(a, b)
    return num

def randDecwSeed(a, b, c):
    random.seed(c)
    num = float(random.uniform(a, b))
    return num
