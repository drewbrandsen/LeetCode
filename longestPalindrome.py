class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_palindrome = ""
        len_palindrome = 0

        # Option 2: for every character, search outward for "palindromicity"
        for idx, ch in enumerate(s):
            if idx == 0:  # base case
                str_palindrome = ch
                len_palindrome = len(str_palindrome)
            else:
                max_length = min(idx-0, len(s)-idx)
                # Even case (middle + right elements equal)
                if ch == s[idx+1]:
                    print("even case")

                # Odd Case
                elif s[idx-1] == s[idx+1]:
                    # Fold string at the character of index
                    l_side = s[idx-max_length:idx]
                    r_side = s[idx+max_length:idx:-1]

                    for i in range(max_length):
                        if l_side[0:i+1] == r_side[0:i+1]:
                            if i+1 > len_palindrome:
                                str_palindrome = s[(idx-i-1):(idx+i+2)]
                                len_palindrome = len(str_palindrome)
                        else:
                            break

                else:
                    continue  # no palindrom with this char at middle

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
