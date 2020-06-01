class Solution:

    def check_palindrome(self, s: str) -> int:
        # Need to search from the middle outward to improve speed
        len_string = len(s)

        if len_string % 2:  # odd string length
            loop_range = int((len_string-1) / 2)
            result_len = 1  # middle char always a match
        else:
            loop_range = int(len_string / 2)
            result_len = 0

        for i in reversed(range(loop_range)):
            if s[i] == s[-i-1]:
                result_len += 2
            else:
                if s[-i-1] == s[0]:
                    return -1# not a palindrome, but some hope
                else:
                    return -1  # not a palindrome, note bad index location

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

            # Find indexes that match the current character 'ch'
            indexes_ch = [i for i, letter in enumerate(s) if letter == ch]

            # Loop over each substring
            for char_idx in reversed(indexes_ch):
                # Only look forward for substrings starting with longest first and must
                # be greater than current max substring
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
    assert(ans == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print("Test 5 - Passed: '" + input_str + "'")

    # Test 6
    input_str = "aaabaaaa"
    ans = solution.longestPalindrome(input_str)
    assert(ans == "aaabaaa")
    print("Test 6 - Passed: '" + input_str + "'")

    # Test 7
    input_str = "abcdbbfcba"
    ans = solution.longestPalindrome(input_str)
    assert(ans == "bb")
    print("Test 7 - Passed: '" + input_str + "'")

    # Test 8
    input_str = "cbcdcbedcbc"
    ans = solution.longestPalindrome(input_str)
    assert(ans == "bcdcb")
    print("Test 8 - Passed: '" + input_str + "'")

    # Test 9
    input_str = "fklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
    ans = solution.longestPalindrome(input_str)
    assert(ans == "fklkf")
    print("Test 9 - Passed: '" + input_str + "'")

    # Test 10
    input_str = "321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123"
    ans = solution.longestPalindrome(input_str)
    assert(ans == "321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123")
    print("Test 10 - Passed: '" + input_str + "'")