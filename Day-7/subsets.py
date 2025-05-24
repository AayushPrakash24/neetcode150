class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking solutoin
        # TC: O(n * 2^n) SC: O(n * 2^n)
        n = len(nums)
        ret = []

        def backtrack(idx, path):
            ret.append(path[:])

            for i in range(idx,n):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        
        backtrack(0,[])
        return ret
        
        # iterative version
        # TC: O(n * 2^n) SC: O(n * 2^n)

        ret = [[]]

        for num in nums:
            newSubsets = []
            for path in ret:
                temp = path[:]
                temp.append(num)
                newSubsets.append(temp)
            ret.extend(newSubsets)

        return ret




