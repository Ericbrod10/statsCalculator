def division(a, b):
    b = float(b)
    if b == 0:
        c = 0
        raise Exception('Cannot divide by 0.')
    else:
        a = float(a)
        c = round(a / b, 9)
        return c
