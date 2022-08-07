def intToRoman(num):
  romans = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 100 : 'M'}
  ans = ''
  #1000s
  if num >= 1000:
    for i in range(num, 0, -1000):
      ans = ans + 'M'
      num = num - 1000
  if num % 1000 >= 900 and num % 1000 < 1000:
    ans = ans + 'CM'
    num = num - 900
  #500s
  if num >= 500 and num < 600:
    ans = ans + 'D'
    num = num - 500
  if num % 1000 >= 400 and num % 1000 < 500:
    ans = ans + 'CD'
    num = num - 400
  #100s
  if num >= 100:
    for i in range(num, 0, -100):
      ans = ans + 'C'
      num = num - 100
  if num % 100 >= 90 and num % 100 < 100:
    ans = ans + 'XC'
    num = num - 90
  #50s
  if num >= 50 and num < 60:
    ans = ans + 'L'
    num = num - 50
  if num % 100 >= 40 and num % 100 < 50:
    ans = ans + 'XL'
    num = num - 40
  #10s
  if num >= 10:
    for i in range(num, 0, -10):
      ans = ans + 'X'
      num = num - 10
  if num % 10 == 9:
    ans = ans + 'IX'
    num = num - 9 # may be omitted
  #5s
  if num >= 5:
    ans = ans + 'V'
    num = num - 5
  if num % 10 == 4:
    ans = ans + 'IV'
    num = num - 4 # may be omitted
  #1s
  if num >= 1:
    for i in range(num, 0, -1):
      ans = ans + 'I'
      num = num - 1
  return ans

#Tests
print(intToRoman(1994))