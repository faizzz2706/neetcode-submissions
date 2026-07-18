class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []

        def solve(perm, visited):
            if len(perm) == len(nums):
                self.ans.append(list(perm))
                return
            
            for i in range(len(nums)):
                if nums[i] in visited:
                    pass
                
                else:
                    perm.append(nums[i])
                    visited.add(nums[i])
                    solve(perm, visited)
                    perm.pop()
                    visited.remove(nums[i])
        
        solve([], set())
        
        return self.ans