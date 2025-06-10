class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ret = []

        def backtrack(path, index):
            if index >= n:
                ret.append(path[:])

            for i in range(index+1,n+1):
                if s[index:i] == s[index:i][::-1]:
                    path.append(s[index:i])
                    backtrack(path, i)
                    path.pop()
        
        backtrack([],0)
        return ret


            
        