def dig_pow(n: int, p: int):
    # your code
    s = sum(int(d)**(p+i) for i, d in enumerate(str(n)))
    return s // n if s % n == 0 else -1
​