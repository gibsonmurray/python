from ast import Num


print("Type 1 to enter a number or 2 to enter a name:\n")
x = input()
if x == 1:
  print("Enter player number:\n")
  x = input()
  if x is 10 or x is 16 or x is 36 or x is 19:
    print("Which player wears number " + x + " on his jersey?\n")
    