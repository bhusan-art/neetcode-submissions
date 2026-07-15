class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [0]*26
        arr2 = [0]*26
        if len(s) > len(t) or len(t) > len(s):
            return False
        for i in range(len(s)):
            arr1[ord(s[i])- ord('a')] +=  1

        for j in range(len(t)):
            arr2[ord(t[j]) - ord('a')] +=  1
        
        if arr1 == arr2:
            return True
        else:
            return False


    #METHOD 2
        # c = {}
        # if len(s) != len(t):
        #     return False
        
        # for i in s:
        #     c[i] =  c.get(i,0)  + 1 ;
        # for i in t:
        #     c[i] =  c.get(i,0) - 1;
        #     if c[i] < 0:
        #         return False
        # return True
        

        
    
        

        
    

