# https://leetcode.com/problems/valid-parentheses/description/
# ord numbers
# ( 40
# ) 41
# { 123
# } 125
# [ 91
# ] 93

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        res = []
        if len(s) % 2 == 0:
            for i in s:
                if i in '({[':
                    stack.append(i)
                    pass
                elif stack:
                    if i == ')' and ord(stack.pop()) == 40:
                        res.append(True)
                    elif i == ']' and ord(stack.pop()) == 91:
                        res.append(True)
                    elif i == '}' and ord(stack.pop()) == 123:
                        res.append(True)
                    else:
                        res.append(False)
                else:
                    res.append(False)
        else:
            return False
        if stack:
           return False 
        return all(res)


case1 = '()' # True
case2 = '(})' # False
case3 = '()[]{}' # True
case4 = '([)]' # False
case5 = '((' # False
case6 = "(){}}{" # False
case7 = '({})' # True
case8 = ")(){}" # False
case9 = "))" # False
case10 = '}([]){' # False


print(Solution().isValid(case1))
print(Solution().isValid(case2))
print(Solution().isValid(case3))
print(Solution().isValid(case4))
print(Solution().isValid(case5))
print(Solution().isValid(case6))
print(Solution().isValid(case7))
print(Solution().isValid(case8))
print(Solution().isValid(case9))
print(Solution().isValid(case10))
