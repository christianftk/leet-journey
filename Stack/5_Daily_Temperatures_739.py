class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                sTemp, sIndex = stack.pop()
                answer[sIndex] = (index - sIndex)
            stack.append([temp, index])          
        return answer


temperatures1 = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]
print(Solution.dailyTemperatures(Solution, temperatures1))
print(Solution.dailyTemperatures(Solution, temperatures2))