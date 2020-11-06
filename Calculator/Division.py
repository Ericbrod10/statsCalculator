def division(a, b):
    if b == '0':
        c = 0
        print('Cannot divide by 0.')
        return c
    else:
        a = float(a)
        b = float(b)
        c = round(a / b, 9)
        return c
