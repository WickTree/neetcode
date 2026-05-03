class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[0] * len(nums)
        for i in range(0,len(nums)):
            prod=1
            for j in range(0,len(nums)):
                if j==i:
                    continue
                prod *= nums[j]
            out[i] = prod
        return out


        