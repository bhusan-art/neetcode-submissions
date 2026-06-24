class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,n = 0,len(numbers)-1

        while l<n:
            cum = numbers[l] +  numbers[n];
            if cum > target:   # 1+4 = 5 > 3
                n -= 1
            elif cum < target:   # 1+1 = 2 < 3:
                l += 1
            else:
                return [l+1,n+1]
            
        return []
                
 