class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Basically Kadanes algo
        # TC: O(n) SC: O(1)

        current = nums[0]
        maximum = nums[0]

        for num in nums[1:]:
            if current < 0:
                current = num
            else:
                current += num
            
            maximum = max(maximum, current)

        return maximum
            
        