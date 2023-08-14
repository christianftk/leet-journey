"""
    The idea is to fill a hashset while iterating over the array.
    To find the longest consecutive, iterate over the set and 
    check for previous numbers and consecutive numbers (constant time access being a set) and remove them as you count
"""

class Solution:
    def getConsecutive(self, map: set, x: int) -> int:
        if x not in map: 
            return 0
        consec = 1
        map.remove(x)
        iter = x - 1
        while iter in map:
            map.remove(iter)
            iter -= 1
            consec += 1
        iter = x + 1
        while iter in map:
            map.remove(iter)
            iter += 1
            consec += 1
        return consec
        
    def longestConsecutive(self, nums: list[int]) -> int:
        map = set(nums)
        res = 0
        for x in nums:
            tmp = Solution.getConsecutive(self, map, x)
            if tmp > res:
                res = tmp
        return res

nums = [100,4,200,1,3,2]
print(Solution.longestConsecutive(Solution, nums))