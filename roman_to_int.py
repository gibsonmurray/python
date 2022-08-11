def intToRoman(num):
  romans = {1000 : 'M',900 : 'CM',  500 : 'D', 400 : 'CD', 100 : 'C', 90 : 'XC', 
            50 : 'L', 40 : 'XL', 10 : 'X', 9 : 'IX', 5: 'V', 4 : 'IV', 1: 'I'}
  ans = ''
  while num > 0:
    for key in romans:
      while num / key > 1:
        ans = ans + romans.get(key)
        num = num // key
  return ans

#Tests
print(intToRoman(1994))