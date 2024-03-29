
# Leetcode : https://leetcode.com/problems/sequential-digits/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        def generate_sequential(num, current_digit):
            if low <= num <= high:
                result.append(num)

            if num > high or current_digit > 9:
                return

            next_digit = current_digit + 1
            if next_digit <= 9:
                generate_sequential(num * 10 + next_digit, next_digit)

        for start_digit in range(1, 10):
            generate_sequential(start_digit, start_digit)

        return sorted(result)
