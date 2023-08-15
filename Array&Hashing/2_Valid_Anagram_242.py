class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


        """ 
        Time can be improved, too much memory
        if len(s) == len(t):
            if sorted(s) == sorted(t):
                return True
        return False """

s1 = "anagram"
s2 = "nagaram"
print(Solution.isAnagram(Solution,s1,s2))

s1 = "rat"
s2 = "car"
print(Solution.isAnagram(Solution,s1,s2))
