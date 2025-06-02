class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        n = len(nums)

        for i in range(n-2):
            j,k = i+1, n-1

            if (i > 0 and nums[i] == nums[i-1]):
                continue

            while j < k:
                val = nums[i]+nums[j]+nums[k]
                if val == 0:
                    triplets.add((nums[i],nums[j],nums[k]))
                if val > 0:
                    k -= 1
                else:
                    j += 1
        
        return list(triplets)
                






