class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        front = 0
        End = len(heights)-1  
        for i in range(End):
            choose = min(heights[End], heights[front])

            area = choose  * (End - front)
            if res < area:  
                res = area
            if heights[End] > heights[front]:
                front +=  1
            else:
                End -= 1
        return res