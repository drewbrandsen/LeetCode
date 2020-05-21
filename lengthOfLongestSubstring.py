class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Key is detecting repeated letters
        letter_dict = {}
        max_substring = 0

        for idx, char in enumerate(s):
            # Place every char into the dictionary
            if char not in letter_dict.keys():
                letter_dict[char] = idx

            # If the char already exists in the dictionary
            else:
                # Get length of found substring (repeated char means end
                # of substring found)
                len_substring = idx - letter_dict[char]

                # Update index for this char since substring starts over
                letter_dict[char] = idx

                # If new substring is the record, update max
                if len_substring > max_substring:
                    max_substring = len_substring

        # Return max substring length
        return max_substring


if __name__ == "__main__":

    solution = Solution()
    # Test 1
    input_str = "abcabcbb"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans == 3)
    print("Test 1 - Passed: " + input_str)

    # Test 1
    input_str = "bbbbb"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans == 1)
    print("Test 2 - Passed: " + input_str)

    # Test 1
    input_str = "pwwkew"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans == 3)
    print("Test 3 - Passed: " + input_str)
