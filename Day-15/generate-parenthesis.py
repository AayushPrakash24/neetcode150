class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def backtrack(path,l,r):
            if len(path) == n*2:
                ret.append(''.join(path[:]))
            
            if l < n:
                path.append('(')
                backtrack(path, l+1, r)
                path.pop()
            
            if r < l:
                path.append(')')
                backtrack(path,l,r+1)
                path.pop()
        
        backtrack([],0,0)
        return ret
