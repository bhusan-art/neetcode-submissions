class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = {}
        if len(s) != len(t):
            return False
        
        for i in s:
            c[i] =  c.get(i,0)  + 1 ;
        for i in t:
            c[i] =  c.get(i,0) - 1;
            if c[i] < 0:
                return False
        return True
        


        