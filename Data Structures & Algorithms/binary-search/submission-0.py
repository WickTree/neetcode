class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j=-1
        for i in range(0,len(nums)):
            if nums[i]==target:
                j=i
        return j
            