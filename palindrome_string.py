def longestPalindrome(s: str) -> str:
  max_index = 0
  max_length = 0
  possible_pals = []
  for i in range(len(s)):
    for j in range(len(s) - 1, 0, -1):
      if s[i] == s[j]:
        possible_pals.append([s[i:j + 1], len(s[i:j + 1])]) # i=0: possible palindrome, i=1: length
  for pal in possible_pals:
    for i in range(len(pal[0]) // 2):
      if pal[0][i] == pal[0][-i] and pal[1 > max_length]:
        max_index = possible_pals.index(pal)
  return possible_pals[max_index][0]

print(longestPalindrome("babad"))