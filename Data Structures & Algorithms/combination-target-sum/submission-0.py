class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def findcomb(idx, total, path):
            if total == target:
                res.append(path[:])
                return
            
            if total > target or idx >= len(nums):
                return

            curr = total + nums[idx]
            path.append(nums[idx])
            findcomb(idx, curr, path)
            path.pop()
            findcomb(idx+1,total, path)
        findcomb(0,0,[])
        return res