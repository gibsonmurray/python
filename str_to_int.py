import re

def myAtoi(s: str) -> int:
    s = s.strip()
    if s != str.empty:
        sign = s[:1]
        ans = re.search("^\d", s[1:])
        ans = int(ans)
        
        