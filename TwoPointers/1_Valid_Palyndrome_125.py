class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if not((s[i] <= 'z' and s[i] >= 'a') or (s[i] <= 'Z' and s[i] >= 'A') or ((s[i] <= '9' and s[i] >= '0'))):
                i += 1
                continue
            if not((s[j] <= 'z' and s[j] >= 'a') or (s[j] <= 'Z' and s[j] >= 'A') or ((s[j] <= '9' and s[j] >= '0'))):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
    
s1 = "A man, a plan, a canal: Panama"
s2 = "0P"
print(Solution.isPalindrome(Solution,s2))
print(Solution.isPalindrome(Solution,s1))