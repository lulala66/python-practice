class Solution:
    """
    Given a string containing just the characters
    '(', ')', '{', '}', '[' and ']', determine if
    the input string is valid. The brackets must
    close in the correct order, "()" and "()[]{}"
    are all valid but "(]" and "([)]" are not.
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in dic.keys():
                stack.append(char)
            elif char in dic.values():
                if stack == [] or char != dic[stack[-1]]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        return stack == []
