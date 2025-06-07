class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()

        def backtrack(out, index, curr):
            if curr == target:
                ret.append(out[:])
                return
            if curr > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                out.append(candidates[i])
                backtrack(out, i+1, curr + candidates[i])
                out.pop()

        backtrack([],0,0)
        return ret
