class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        bracket_dict = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in s:
            if i in bracket_dict.values():
                stack.append(i)

            elif i in bracket_dict:
                if not stack or stack[-1] != bracket_dict[i]:
                    return False
                
                stack.pop()
            
            else:
                return False
        
        return not stack