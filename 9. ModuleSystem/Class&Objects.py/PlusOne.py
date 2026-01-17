'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        # Case 1: last digit < 9
        if digits[i] < 9:
            digits[i] += 1
            return digits

        # Case 2: last digit == 9 → carry
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        if i >= 0:
            digits[i] += 1
            return digits

        # Case 3: all digits were 9
        return [1] + digits
    '''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1     # start from last digit

        if digits[i] < 9:
            digits[i] += 1
            return digits

        # if last digit is 9
        digits[i] = 0
        digits[i-1] += 1
        return  [1] + digits