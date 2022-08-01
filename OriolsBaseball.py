players = {
  "Jones" : 10,
  "Mancini" : 16,
  "Joseph" : 36,
  "Davis" : 19
}
print("Type 1 to enter a number or 2 to enter a name: ")
n = input()
if n is 1:
  print("\nEnter player number: ")
  n = input()
  if n is 10 or n is 16 or n is 36 or n is 19:
    print("\nWhich player wears number " + n + " on his jersey? ")
    name = input()
    if name