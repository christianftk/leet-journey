class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []

        # Scan the heights array and fill a stack which contains only the pairs of rectangles that can still grow
        # if the following height is smaller than the top of the stack, the top is to be popped and the area calculated

        for index, height in enumerate(heights):
            #print(stack)
            if stack:
                top = stack[-1]
                if top[1] < height:
                    stack.append([index,height])
                    continue
                elif top[1] == height:
                    stack.append([top[0],height])
                    continue
                while top[1] > height:
                    stack.pop()
                    maxArea = max(maxArea, (index - top[0]) * top[1])
                    #print(f"dopo aver tolto {top} la maxArea e' {maxArea}")
                    toAdd = [top[0], height]
                    if stack: top = stack[-1]
                    else: break
                stack.append(toAdd)
            else:
                stack.append([index,height])
        
        # After scanning the heights array, the stack could still contain the pairs of rectangles
        # whose width goes from their index to the end of the array
        while stack:
            top = stack[-1]
            stack.pop()
            maxArea = max(maxArea, (len(heights) - top[0]) * top[1])    
        #print(stack)
        return maxArea
    
heights1 = [2,1,5,6,2,3]
#heights2 = [2,4]
#heights3 = [2,4,3]
print(Solution.largestRectangleArea(Solution, heights1))
#print(Solution.largestRectangleArea(Solution, heights2))
#print(Solution.largestRectangleArea(Solution, heights3))