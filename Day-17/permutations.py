class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def backtrack(path):
            if len(path) == len(nums):
                ret.append(path[:])
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()
        
        backtrack([])
        return ret