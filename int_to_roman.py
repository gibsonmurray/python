def romanToInt(s):
  romans = {'M' : 1000, 'CM' : 900, 'D' : 500, 'CD' : 400, 'C' : 100, 'XC' : 90, 
            'L' : 50, 'XL' : 40, 'X' : 10, 'IX' : 9, 'V' : 5, 'IV' : 4, 'I' : 1,}
  ans = 0
  for key in romans:
    if len(key) > 1:
      while key in s[:2]:
        ans = ans + romans.get(key)
        s = s[2:]
    else:
      while key in s[:1]:
        ans = ans + romans.get(key)
        s = s[1:]
  return ans

#Testing
print(romanToInt('MCMXCIV'))