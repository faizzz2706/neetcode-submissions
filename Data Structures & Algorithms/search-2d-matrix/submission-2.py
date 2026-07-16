class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        c = col-1
        r = 0
        low = 0
        high = col-1
        while r < row and c < col:

            if matrix[r][low] <= target <= matrix[r][high]:
                while low <= high:
                    mid = low + (high-low)//2
                    if matrix[r][mid] == target:
                        return True
                    elif matrix[r][mid] > target:
                        high = mid-1
                    else:
                        low = mid + 1
                
                return False

            else:
                r = r + 1
                high = c = col -1
                low = 0
                
        
        return False