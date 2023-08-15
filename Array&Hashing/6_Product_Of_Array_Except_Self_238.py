"""
    "The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer"
    According to the constraint then I could save the product of all the elements
    and return an array where each element is product/nums[i]

    Main problem is that you have to consider 0s
    If there's one 0 it means that in the output it'll be the only one with a non-zero value
    if there's two 0s it means the whole output is 0

    NOTE: After finishing the exercise I've noticed division wasn't allowed
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        product = 1
        nzeros = 0
        for i in nums:
            if nzeros < 2:
                if i is 0:
                    nzeros += 1
                else:
                    product *= i
            else:
                product = 0
                break

        for num in nums:
            if nzeros > 1:
                res.append(0)
            else:
                if num is 0:
                    res.append(int(product))
                else:
                    if nzeros < 1:
                        res.append(int(product/num))
                    else:
                        res.append(0)
        return res

nums = [1,2,3,4]
print(Solution.productExceptSelf(Solution,nums))
