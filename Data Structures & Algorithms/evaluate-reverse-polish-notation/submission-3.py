class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
        "+": lambda x, y: int(x) + int(y),
        "-": lambda x, y: int(x) - int(y),
        "*": lambda x, y: int(x) * int(y),
        "/": lambda x, y: int(x) / int(y)}
        stk = []
        for c in tokens:
            if c in ops:
                y = stk.pop()
                x = stk.pop()
                stk.append(ops[c](x, y))
            else:
                stk.append(c)
        return int(stk[-1])


