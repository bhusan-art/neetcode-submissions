class Solution:
    def trap(self, height: List[int]) -> int:
        start   = 0
        end  = len(height) - 1
        water = 0
        leftMax = height[start]
        rightMax = height[end] 

        while start < end:   #0,2,0,3,1,0,1,3,2,1
            if leftMax <= rightMax:
                start += 1
                leftMax = max(leftMax, height[start])
                water += leftMax - height[start]
            else:
                end -= 1
                rightMax = max(rightMax,height[end])
                water += rightMax - height[end]

        return water

