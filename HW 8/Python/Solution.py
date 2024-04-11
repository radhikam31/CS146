class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency_map = {}
        for char in s:
            frequency_map[char] = frequency_map.get(char, 0) + 1
        max_length = 0
        odd_frequency_seen = False
        for frequency in frequency_map.values():
            if frequency % 2 == 0:
                max_length += frequency
            else:
                max_length += frequency - 1
                odd_frequency_seen = True
        return max_length + 1 if odd_frequency_seen else max_length

solution = Solution()
s1 = "abccccdd"
print("Test Case 1:", solution.longestPalindrome(s1))  # Output: 7

s2 = "speediskey"
print("Test Case 2:", solution.longestPalindrome(s2))  # Output: 5
