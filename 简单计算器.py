# leetcode 224
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        oper = []
        num = []

        def cal(o, n1, n2):
            if o == '+':
                return n1 + n2
            return n2 - n1

        for i, v in enumerate(s):
            if v.isdigit():
                if i > 0 and s[i - 1].isdigit():
                    num.append(num.pop() * 10 + int(v))
                else:
                    num.append(int(v))
            elif v == ' ':
                continue
            elif v == '(':
                oper.append('(')
            elif v == ')':
                while oper[-1] != '(':
                    o = oper.pop()
                    num.append(cal(o, num.pop(), num.pop()))
                oper.pop()
            elif v in ['+', '-']:
                if oper and oper[-1] in ['+', '-']:
                    o = oper.pop()
                    num.append(cal(o, num.pop(), num.pop()))
                oper.append(v)
        while oper:
            o = oper.pop()
            num.append(cal(o, num.pop(), num.pop()))
        return num[-1]


print(Solution().calculate("((1+(4+5+2)-3)+(6+8))"))
