class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in nums[i+1:]:
                return [i,nums[i+1:].index(tmp) + i + 1]
        return []
        """ 
        First quick solution, could improve the time
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
        return [] """
    
nums = [2,7,11,15]
target = 22
print(Solution.twoSum(Solution, nums, target))
