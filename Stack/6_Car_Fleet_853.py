class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


target1 = 12
position1 = [10,8,0,5,3]
speed1 = [2,4,1,1,3]
target2 = 100
position2 = [0,2,4]
speed2 = [4,2,1]
print(Solution.carFleet(Solution,target1,position1,speed1))
print(Solution.carFleet(Solution,target2,position2,speed2))