def reverse(x: int) -> int:
    if x > (2**31) - 1 or x < -2**31:
        return 0
    s = str(x)
    arr = []
    negative = False
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '-':
            negative = True
        else:
            arr.append(s[i])
    s = "".join(str(elem) for elem in arr)
    ans = int(s)
    if negative:
        ans *= -1
    if ans > (2**31) - 1 or ans < -2**31:
        return 0
    return ans