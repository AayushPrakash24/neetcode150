class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashmap solution 
        # TC: O(n) SC: O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False