class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        myset = {s[0]}

        i = 0
        j = i + 1
        curr = 1
        max_len = 1
        while j < len(s):
            if s[j] not in myset:
                myset.add(s[j])
                curr += 1
                max_len = max(curr, max_len)
                j += 1
            
            else:
                myset.remove(s[i])
                curr -= 1
                i += 1
        
        return max_len
