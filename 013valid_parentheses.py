# -*- coding: utf-8 -*-
class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char in ["(","{","["]:
                stack.append(char)
            elif not stack:     #针对单括号的问题,直接报错.
                return False
            elif (char == ")") and (stack[len(stack)-1]=="("):
                stack.pop()
            elif (char == "}") and (stack[len(stack)-1]=="{"):
                stack.pop()
            elif (char == "]") and (stack[len(stack)-1]=="["):
                stack.pop()
            else:
                return False


        return len(stack)==0

if __name__ =='__main__':
    print(Solution().isValid("[]"))

# 注意:
# 这里给列表中放进一对就移除一对.因此会有stack[len(stack)一说.
# pop()函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。