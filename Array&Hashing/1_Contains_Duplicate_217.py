

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash
        res = set()
        for i in nums:
            if i in res:
                return True
            res.add(i)
        
        return False

        """ 
        ## Fast Solution, but too much memory ##
        res = {}
        for i in nums:
            if(i not in res):
                res[i] = 1
            else:
                return True
        return False 
        """

        """ 
        ## Time Limit Exceeded ##
        for i in nums:
            if i in nums[(nums.index(i)+1):]:
                return True
            
        return False 
        """


num = [1,2,3,1]
print(Solution.containsDuplicate(Solution, num))
