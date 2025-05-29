class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hashmaps and visiting
        # TC: O(n) SC: O(n)
        
        hashset = set(nums)
        visited = set()

        maximum = 0

        for num in nums:
            if num - 1 in hashset or num in visited:
                continue
            
            val = num
            while val + 1 in hashset:
                visited.add(val)
                val += 1
            
            maximum = max(maximum, val-num+1)

        return maximum



    