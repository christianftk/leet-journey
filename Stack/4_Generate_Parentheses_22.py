class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []

        def generator(openCount, closeCount):
            if openCount == closeCount == n:
                res.append("".join(stack))
                return

            if openCount < n:
                stack.append("(")
                generator(openCount + 1, closeCount)
                stack.pop()
            if closeCount < openCount:
                stack.append(")")
                generator(openCount, closeCount + 1)
                stack.pop()
        
        generator(0,0)
        return res
n = 3
print(Solution.generateParenthesis(Solution,n))