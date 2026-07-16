class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):

            if not stack:
                res[i] = 0
                stack.append(i)
            
            else:

                while stack:
                    if temperatures[stack[-1]] > temperatures[i]:
                        res[i] = stack[-1] - i
                        break
                    else:
                        stack.pop()
                
                stack.append(i)
                
        
        return res