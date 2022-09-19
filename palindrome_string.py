def longestPalindrome(s: str) -> str:
  if len(s) == 1:
    return s
  max_index = 0
  max_length = 0
  possible_pals = []
  for i in range(len(s)):
    for j in range(len(s) - 1, 0, -1):
      if s[i] == s[j]:
        possible_pals.append([s[i:j + 1], len(s[i:j + 1])]) # i=0: possible palindrome, i=1: length
  for pal in possible_pals:
    verify = True
    for i in range(len(pal[0]) // 2):
      if pal[0][i] != pal[0][-i - 1]:
        verify = False
      if not verify:
        i = len(pal[0]) // 2
    if not verify:
      continue
    if pal[1] > max_length:
        max_length = pal[1]
        max_index = possible_pals.index(pal)
  return possible_pals[max_index][0]

print(longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))