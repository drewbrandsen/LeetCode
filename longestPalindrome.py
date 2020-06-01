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

            # If the next char is the same as the previous, it can't be the start
            # of a longer palindrome
            if idx > 0 and ch == s[idx-1]:
                break

            # Find indexes that match the current character 'ch'
            indexes_ch = [i for i, letter in enumerate(s) if letter == ch]

            # Loop over each substring
            for char_idx in reversed(indexes_ch):
                # Only look forward for substrings starting with longest first
                if (char_idx - idx) < len_palindrome:
                    break
                if idx <= char_idx:
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

    # Test 4
    input_str = "ac"
    ans = solution.longestPalindrome(input_str)
    assert(ans == "a" or ans == "c")
    print("Test 4 - Passed: '" + input_str + "'")

    # Test 5
    input_str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ans = solution.longestPalindrome(input_str)
    assert(ans == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print("Test 5 - Passed: '" + input_str + "'")