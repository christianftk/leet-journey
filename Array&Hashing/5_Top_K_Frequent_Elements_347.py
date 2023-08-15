"""
    -Sorting the array and then counting? Sorting takes time
    
    -Using a hashtable to do the counting of the occurences
     Sort the table by the values
     Get the keys for k times


"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        res = []
        # sorting over items let me use the lambda to specify that i sort over values (index 0 is key, index 1 is value)
        for max in sorted(count.items(), key=lambda x:x[1], reverse=True):
            if (k > 0):
                res.append(max[0])
                k -= 1
            else:
                return res

        return res

nums = [3,3,1,1,1,2,2,3]
k = 2
print(Solution.topKFrequent(Solution, nums, k))
