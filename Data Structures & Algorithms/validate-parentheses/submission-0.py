class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mp = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in "({[":
                stack.append(char)

            else:
                if not stack:
                    return False

                if stack[-1] == mp[char]:
                    stack.pop()
                else:
                    return False

        return not stack