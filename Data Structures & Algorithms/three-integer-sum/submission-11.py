class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i> 0  and nums[i] == nums[i-1]:
                continue
            l = i+1
            e = len(nums)-1         #-4,-1,-1,0,1,2
            while l < e:
                s = nums[i] + nums[l] + nums[e]

                if s == 0:
                    res.append([nums[i],nums[l],nums[e]])
                    l += 1
                    e -= 1
                    while l < e and nums[l] == nums[l-1]:
                        l += 1
                    while l < e and nums[e] == nums[e+1]:
                        e -= 1
                elif s < 0:
                    l += 1
                else:
                    e -= 1
                
        return res
                    