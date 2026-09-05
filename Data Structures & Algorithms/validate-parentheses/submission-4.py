class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s: 
            if i in "{([": stack.append(i)
            elif len(stack) == 0: stack.append(i)
            elif i == ")":
                if stack[-1] == "(": stack.pop()
                else: stack.append(i)
            elif i == "}":
                if stack[-1] == "{": stack.pop()
                else: stack.append(i)
            elif i == "]":
                if stack[-1] == "[": stack.pop()
                else: stack.append(i)
        return len(stack) == 0