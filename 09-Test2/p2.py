def p2(arr: list):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]