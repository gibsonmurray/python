def romanToInt(s):
  romans = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
  ans = 0
  #subtraction cases
  if 'IV' in s:
    ans = ans + 4
    index = s.index('IV') #get index of substring
    s = s[:index] + s[index + 2:] #remove substring using slicing + concatenation (2 for 2 characters)
  if 'IX' in s:
    ans = ans + 9
    index = s.index('IX')
    s = s[:index] + s[index + 2:]
  if 'XL' in s:
    ans = ans + 40
    index = s.index('XL')
    s = s[:index] + s[index + 2:]
  if 'XC' in s:
    ans = ans + 90
    index = s.index('XC')
    s = s[:index] + s[index + 2:]
  if 'CD' in s:
    ans = ans + 400
    index = s.index('CD')
    s = s[:index] + s[index + 2:]
  if 'CM' in s:
    ans = ans + 900
    index = s.index('CM')
    s = s[:index] + s[index + 2:]
  #all other letters
  for letter in s:
    ans = ans + romans.get(letter)
  return ans

#Testing
print(romanToInt('I'))