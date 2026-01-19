class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        result = 0
        while a >= b:
            temp, multiple = b, 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            result += multiple


        # Apply sign
        if (dividend < 0) ^ (divisor < 0):
            result = -result

        # Clamp
        return max(INT_MIN, min(INT_MAX, result))
