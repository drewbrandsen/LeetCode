class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Solution is detecting repeated letters
        substring = []
        max_substring = 0 # initialize to empty case

        for char in s:
            # Place every char into the substring list, currently UPPER and lower are
            # considered unique
            if char in substring:
                # Remove repeat char and any preceeding chars
                substring = substring[substring.index(char) + 1:]

            # Add new char
            substring.append(char)

            # Update length and max if needed
            max_substring = max(max_substring, len(substring))

        # Return max substring length
        return max_substring


if __name__ == "__main__":

    solution = Solution()
    # Test 1
    input_str = "abcabcbb"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans == 3)
    print("Test 1 - Passed: '" + input_str + "'")

    # Test 2
    input_str = "bbbbb"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans == 1)
    print("Test 2 - Passed: '" + input_str + "'")

    # Test 3
    input_str = "pwwkew"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans == 3)
    print("Test 3 - Passed: '" + input_str + "'")

    # Test 4: 1 char
    input_str = " "
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans == 1)
    print("Test 4 - Passed: '" + input_str + "'")

    # Test 5: empty
    input_str = ""
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans == 0)
    print("Test 5 - Passed: '" + input_str + "'")

    # Test 6: no repeating chars
    input_str = "Drew"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans == 4)
    print("Test 6 - Passed: '" + input_str + "'")

    # Test 7:
    input_str = "cdd"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans == 2)
    print("Test 7 - Passed: '" + input_str + "'")

    # Test 8:
    input_str = "abba"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans == 2)
    print("Test 8 - Passed: '" + input_str + "'")

    # Test 9:
    input_str = "aab"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert (ans == 2)
    print("Test 9 - Passed: '" + input_str + "'")

    # Test 10:
    input_str = "tmmzuxt"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert (ans == 5)
    print("Test 10 - Passed: '" + input_str + "'")

    # Test 11:
    input_str = "ohomm"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert (ans == 3)
    print("Test 11 - Passed: '" + input_str + "'")