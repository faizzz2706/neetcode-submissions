class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]

        for i in range(1,len(nums)):
            temp = nums[i-1] * left[i-1]
            left.append(temp)
        
        right = [0]*len(nums)
        right[-1] = 1

        for i in range(len(nums)-2,-1,-1):
            temp = nums[i+1] * right[i+1]
            right[i] = temp
        
        res = []
        for i in range(len(nums)):
            res.append(right[i]*left[i])
        
        return res