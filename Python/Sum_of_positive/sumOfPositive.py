def positive_sum(arr):
    n = 0
    for i in arr:
        if i >= 0:
            n += i
    if n == 0:
        return 0
    else:
        return n
            