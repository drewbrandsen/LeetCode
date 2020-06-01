class Solution:

    def check_palindrome(self, s: str) -> int:

        len_string = len(s)

        if len_string % 2:  # odd string length
            loop_range = int((len_string-1) / 2)
            result_len = 1  # middle char always a match
        else:
            loop_range = int(len_string / 2)
            result_len = 0

        for i in range(loop_range):
            if s[i] == s[-i-1]:
                result_len += 2
            else:
                return -1  # not a palindrome

        return result_len

    def longestPalindrome(self, s: str) -> str:

        str_palindrome = ""
        len_palindrome = 0

        # Base case
        if len(s) == 1:
            return s

        # Loop over every character, this character could be the start
        # of a palindrome, so check other instances of this character
        # in the string and see if it forms the endpoints of a palindrome

        # Loop over every character
        for idx, ch in enumerate(s):
            indexes_ch = [i for i, letter in enumerate(s) if letter == ch]

            # Loop over each substring
            for char_idx in indexes_ch:
                # Only look forward for substrings
                if idx < char_idx:
                    substring = s[idx:char_idx + 1]
                    result_len = self.check_palindrome(substring)
                    if result_len > len_palindrome:
                        len_palindrome = result_len
                        str_palindrome = substring

        return str_palindrome


if __name__ == "__main__":

    solution = Solution()
    # Test 1
    input_str = "babad"
    ans = solution.longestPalindrome(input_str)
    assert(ans == "bab" or ans == "aba")
    print("Test 1 - Passed: '" + input_str + "'")

    # Test 2
    input_str = "cbbd"
    ans = solution.longestPalindrome(input_str)
    assert(ans == "bb")
    print("Test 2 - Passed: '" + input_str + "'")

    # Test 3
    input_str = "a"
    ans = solution.longestPalindrome(input_str)
    assert(ans == "a")
    print("Test 3 - Passed: '" + input_str + "'")
