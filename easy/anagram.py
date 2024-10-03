class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s,t = sorted(s), sorted(t)
        if len(s) != len(t) : return False 
        for i in range(0, len(t)):

            if t[i] != s[i]:
                return False
        return True 
