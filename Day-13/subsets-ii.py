class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ret = []

        def backtrack(path,index):
            ret.append(path[:])

            for i in range(index, n):
                if i != index and i != 0 and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path,i+1)
                path.pop()
        
        backtrack([],0)
        return ret
            
