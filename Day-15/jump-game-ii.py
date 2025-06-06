class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxJump = endJump = 0
        jumps = 0

        for i in range(n-1):
            maxJump = max(maxJump, i + nums[i])

            if i == endJump:
                jumps += 1
                endJump = maxJump
        
        return jumps



