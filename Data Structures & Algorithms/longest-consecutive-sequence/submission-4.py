class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        curr = 0
        max_count = 0
        for num in nums:

            if num - 1 not in nums:
                curr = 1
                ref = num
                for _ in range(len(nums)):
                    if ref+1 in nums:
                        curr += 1
                        ref = ref+1
                    else:
                        break
                max_count = max(max_count, curr)
        return max_count