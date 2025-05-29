import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # typical binary search
        # TC: O(log(n)) SC: O(1)
        l,r = 0, len(nums)-1

        while l <= r:
            m = l + (r-l)//2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        
        return -1
    
        # can insta solve like this (use bisect_left or bisect_right)

        # bisect.bisect_left does a binary search O(log(n)) and tells insertion position to the left
        # bisect.bisect_right does bs and tells insertion position to the right
        i = bisect.bisect_left(nums, target)
        if 0 <= i < len(nums) and nums[i] == target:
            return i
        return -1
    

        
        