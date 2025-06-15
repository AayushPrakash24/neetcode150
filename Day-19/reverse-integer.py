class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        
        rev = 0
        x = abs(x)

        while x:
            x,r = divmod(x,10)
            rev = rev * 10 + r
            if rev > 2 ** 31:
                return 0
                
        return rev * sign
        
