class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = float("inf")
        total = 0

        for right in range(len(nums)):
            #Adding the nums one after other to get target
            total += nums[right]

            # when ever the total is >= target
            while total >= target:
                #calculating the len of numbers participated to get the target
                res = min(right-left+1,res)
                #removing the initial number 
                total -= nums[left]
                #moving the window forward
                left += 1
        return 0 if res==float("inf") else res



