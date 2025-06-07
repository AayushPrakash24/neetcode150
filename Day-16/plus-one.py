class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1

        for i in range(n - 1, -1, -1):
            if carry:
                digits[i] += 1
                if digits[i] >= 10:
                    carry = 1
                    digits[i] %= 10
                else:
                    carry = 0

        if carry:
            return [1] + digits

        return digits
