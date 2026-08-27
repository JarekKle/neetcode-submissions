class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {
            "(": 1,
            ")": -1,
            "{": 2,
            "}": -2,
            "[": 3,
            "]": -3
        }
        stack = []
        for par in s:
            if par_dict[par]<0:
                if len(stack)==0:
                    return False
                if par_dict[par]!=-par_dict[stack[-1]]:
                    return False
                stack.pop()    
            else:
                stack.append(par)
        if len(stack)>0:
            return False
        return True