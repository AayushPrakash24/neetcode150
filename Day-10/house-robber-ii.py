class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp
        # TC: O(n) SC: O(1)
        if len(nums) == 1:
            return nums[0]
        
        def simple_rob(nums):
            prev1,prev2 = 0,0

            for num in nums:
                prev1, prev2 = max(prev1,prev2+num), prev1
            return prev1
        
        return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))
