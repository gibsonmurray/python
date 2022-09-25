def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = []
    numsInNums = {}
    for i in range(1, n + 1):
        numsInNums[i] = False
    for i in range(n):
        numsInNums[nums[i]] = True
    for key in numsInNums.keys():
        if numsInNums[key] == False:
            ans.append(key)
    return ans
    