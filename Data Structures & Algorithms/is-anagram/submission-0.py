class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26

        for char in s:
            idx = ord(char) - 97
            arr[idx] += 1
        
        for char in t:
            idx = ord(char) - 97
            arr[idx] -= 1
        
        for num in arr:
            if num != 0:
                return False
        
        return True