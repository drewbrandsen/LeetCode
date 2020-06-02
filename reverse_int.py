class Solution:
    def reverse(self, x: int) -> int:
        result_str = ""

        # preserve sign
        if x < 0:
            sign = -1
            str_x = str(x)
            str_x = str_x[1:]  # remove sign char
        else:
            sign = 1
            str_x = str(x)

        # Reverse the string (python style)
        result_str = str_x[::-1]

        # Convert back to an int
        result_int = sign * int(result_str)

        # Add overflow checks
        if result_int > 2**31 or result_int < -(2**(31) - 1):
            return 0
        else:
            return result_int


if __name__ == "__main__":
    runSolution = Solution()

    test_str = "Test 1"
    median_ans = runSolution.reverse(123)
    assert median_ans == 321
    print("Passes: " + test_str)

    test_str = "Test 2"
    median_ans = runSolution.reverse(-123)
    assert median_ans == -321
    print("Passes: " + test_str)

    test_str = "Test 3"
    median_ans = runSolution.reverse(120)
    assert median_ans == 21
    print("Passes: " + test_str)

    test_str = "Test 4"
    median_ans = runSolution.reverse(-120)
    assert median_ans == -21
    print("Passes: " + test_str)
