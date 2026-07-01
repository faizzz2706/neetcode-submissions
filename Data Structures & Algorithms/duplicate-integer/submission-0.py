class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        look = set()
        for num in nums:
            if num in look:
                return True
            else:
                look.add(num)
        return False