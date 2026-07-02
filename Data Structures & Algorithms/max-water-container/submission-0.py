class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = float('-inf')
        curr_water = 0
        i = 0
        j = len(heights)-1

        while i < j:
            curr_water = min(heights[i], heights[j])*(j-i)
            max_water = max(curr_water, max_water)

            if heights[i] > heights[j]:
                j -= 1
                continue
            
            if heights[i] < heights[j]:
                i += 1
                continue
            
            if heights[i] == heights[j]:
                i+= 1
        
        return int(max_water)