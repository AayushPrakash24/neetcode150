class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bitwise xor 
        # TC: O(n) SC: O(1)

        ret = 0

        # bitwise operations are like this
            # & is bitwise and
            # | is bitwise or
            # ^ is bitwise xor
            # >> is bitwise right shift
            # << is bitwise left shift
            # ~ is bitwise complement
        # these work as operations on binary representations of numbers

        for num in nums:
            # if we do xor all duplicates will cancel and remaining will be the single number
            ret ^= num
        return ret