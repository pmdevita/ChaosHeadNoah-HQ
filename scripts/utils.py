def zero_pad(num, pad):
    n = str(num)
    return "".join(["0" for i in range(pad-len(n))]) + n

