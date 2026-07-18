class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(idx, total, path):

            if total == target:
                
                res.append(path[:])
                return
            
            if idx >= len(candidates) or total > target:
                return
            
            curr = total + candidates[idx]
            path.append(candidates[idx])
            backtrack(idx+1, curr, path)
            path.pop()
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx+=1
            backtrack(idx+1, total, path)
        
        backtrack(0,0,[])
        return res