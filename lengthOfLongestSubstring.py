class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Key is detecting repeated letters
        substring_dict = {}
        max_substring = 0 # initialize to empty case
        len_substring = 0
        idx_substring_start = 0

        for idx, char in enumerate(s):
            # Place every char into the dictionary, currently UPPER and lower are
            # considered unique
            if char not in substring_dict.keys():
                substring_dict[char] = idx
                # We need this case to cover if we never hit a repeating character
                len_substring = (idx - idx_substring_start) + 1

                # If new substring is the record, update max
                if len_substring > max_substring:
                    max_substring = len_substring

            # If the char already exists in the dictionary
            else:
                # Get length of found substring (repeated char means end
                # of substring found)
                len_substring = idx - idx_substring_start

                # update substring start idx
                idx_substring_start = substring_dict[char] + 1

                # update new idx for this char
                substring_dict[char] = idx

                # If new substring is the record, update max
                if len_substring > max_substring:
                    max_substring = len_substring

        # Return max substring length
        # This is either from subsequent substrings fou nd via repeating
        # chars or a single string with no repeating characters
        return max(len_substring, max_substring)


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