import random


def selectRand_wSeed(a, b=1, c=50):
    # Allow for user to specify how many elements they want to choose but default to 1
    random.seed(c)
    if b == 1:
        element = random.choice(a)
    else:
        element = random.choices(a, k=b)
    return element

