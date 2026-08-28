class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = ['+','-','*','/']
        result = int(tokens[0])
        nums = []
        operation = ''
        for operand in tokens:
            if operand not in signs:
                nums.append(int(operand))
            else:
                operation = operand
            if operation != '':
                num1 = nums.pop()
                num2 = nums.pop()
                if operation=='+':
                    result = num2 + num1
                elif operation=='-':
                    result = num2 - num1
                elif operation=='*':
                    result = num2 * num1
                elif operation=='/':
                    result = int(num2 / num1)
                nums.append(result)
                operation = ''
        return result