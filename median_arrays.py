def findMedianSortedArrays(nums1, nums2) -> float:
  ans = 0
  merged = nums1 + nums2
  merged.sort()
  while len(merged) > 2:
    merged.pop()
    merged.pop(0)
  if len(merged) == 2:
    ans = (merged[0] + merged[1]) / 2
  elif len(merged) == 1:
    ans = merged[0]
  return ans

nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))
