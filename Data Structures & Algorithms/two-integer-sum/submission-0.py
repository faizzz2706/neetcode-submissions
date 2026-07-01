class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mydict = {}

        for i in range(len(nums)):
            if nums[i] in mydict:
                return [mydict[nums[i]], i]
            
            else:
                mydict[target-nums[i]] = i