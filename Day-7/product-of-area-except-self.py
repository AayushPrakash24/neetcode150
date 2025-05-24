class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix products
        # TC: O(n) SC: O(n)

        n = len(nums)
        prefix = [1] * n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i]
        
        suffix = [1] * n
        suffix[n-1] = nums[n-1]

        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i]
        
        ret = [1] * n
        ret[0] = suffix[1]
        ret[-1] = prefix[-2]

        for i in range(1,n-1):
            ret[i] = prefix[i-1] * suffix[i+1]
        
        return ret


        