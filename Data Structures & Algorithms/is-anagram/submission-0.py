class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        C1,C2 = {},{};
        if len(s) != len(t):
            return False
        for k in range(len(s)):
            C1[s[k]] = 1 + C1.get(s[k],0);
            C2[t[k]] = 1 + C2.get(t[k],0);
        
        
        for m in C1:
            if C1[m] != C2.get(m,0):
                return False
        return True
        


        