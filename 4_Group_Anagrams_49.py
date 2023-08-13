from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # all available letters
            for c in s:
                 count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return res.values()

        """     
        def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT 
        """
        """ res = []
        for index, s in enumerate(strs):
            print(index,s)
            if s not in res:
                continue
            toAdd = [s]
            for t in strs[(index + 1):]:
                if t not in res:
                    continue
                if self.isAnagram(self,s,t):
                    toAdd.append(t)
            res.append(toAdd)
        return res 
        """
        """     
        Too much time
        res = []
        for s in strs:
            found = False
            for t in res:
                if Solution.isAnagram(self,s,t[0]):
                    print (t[0])
                    t.append(s)
                    found = True
                    break
            if not found:
                    res.append([s]) 
        
        return res
        """

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(Solution, strs))