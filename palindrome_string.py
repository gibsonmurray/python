def longestPalindrome(s: str) -> str:
  for i in range(len(s)):
    for j in range(len(s), 0):
      if s[i] == s[j]:
        str = s[i:j]
        
        