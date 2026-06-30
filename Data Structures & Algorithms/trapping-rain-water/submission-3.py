class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0
        e = len(height) - 1
        water = 0
        leftMax = height[s]
        rightMax = height[e]
        

        while s < e:
            if height[s] < height[e]:
                s += 1
                leftMax = max(height[s],leftMax)
                water +=  leftMax - height[s]
                
            else:
                e -= 1
                rightMax =  max(height[e],rightMax)
                water += rightMax - height[e]
                
        return water
                

