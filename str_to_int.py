from operator import truediv
import re

def myAtoi(s: str) -> int:
    s = s.strip()
    negative = False
    if s[:1] == "-":
        negative = True
        ans = int(re.search("^\d", s[1:]).string)
    else: 
        ans = int(re.search("^\d", s).string)
    if (-2)**31 > ans or ans > (2**31) - 1:
        ans = 0
    if negative:
        ans *= (-1)
    return ans

myAtoi("4193 with words")        