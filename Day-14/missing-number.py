class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)

        # return ((n * (n+1)) // 2) - sum(nums)
        
        ret = len(nums)
        for i,num in enumerate(nums):
            ret ^= i^num

        return ret

    