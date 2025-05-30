class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # TC: O(n^( (target/min(candidates)) + 1)) SC: O(target/min(candidates))
        n = len(candidates)
        ret = []
        def backtrack(index, path, runningSum):
            if runningSum == target:
                ret.append(path[:])
                return
            if runningSum > target:
                return
            
            for i in range(index, n):
                path.append(candidates[i])
                backtrack(i, path, runningSum + candidates[i])
                path.pop()
        
        backtrack(0, [], 0)
        return ret