class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Key is detecting repeated letters
        letter_dict = {}

        for idx, char in enumerate(s):
            print(idx)

        return 5




if __name__ == "__main__":

    solution = Solution()
    # Test 1
    input_str = "abcabcbb"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans) == 3
    print("Test 1 - Passed: " + input_str)

    # Test 1
    input_str = "bbbbb"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans) == 1
    print("Test 2 - Passed: " + input_str)

    # Test 1
    input_str = "pwwkew"
    ans = solution.lengthOfLongestSubstring(input_str)
    assert(ans) == 3
    print("Test 3 - Passed: " + input_str)
