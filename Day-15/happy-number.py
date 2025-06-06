class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def make_happy(num):
            ret = 0
            while num > 0:
                num, r = divmod(num,10)
                ret += r ** 2
            return ret
        
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = make_happy(n)
        return True
