class Solution:
    def isValid(self, s: str) -> bool:
        #check if len of string is even if not return false
        #put half of string in stack
        #pop from stack and compare with first of remaining string
        #if even one doesnt match set to False,else True
        stack=[]
        pair = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in pair:
                if not stack or stack[-1] != pair[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack
        



        