def find_outlier(integers):
    odd = []
    even = []
    for i in integers:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]