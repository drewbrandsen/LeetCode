class Solution:
    def myAtoi(self, str: str) -> int:
        
        MAX_INT = (2**31) - 1
        MIN_INT = (-2**31)
        result_str = ""
        detect_num = False
        negative_char = 0
        positive_char = 0

        # Loop over every character to detect numbers
        for ch in str:
            if ch == " ":
                if detect_num is False:
                    # If we detect whitespace after a hyphen this is invalid
                    if negative_char == 1 or positive_char == 1:
                        return 0
                    else:
                        continue
                else:
                    break

            elif ch == "-":
                if positive_char == 1 or negative_char == 1:
                    return 0  # cannot have duplicate sign chars
                elif detect_num is False:
                    negative_char = 1
                    continue
                else:
                    break

            elif ch == "+":
                if positive_char == 1 or negative_char == 1:
                    return 0  # cannot have duplicate sign chars
                elif detect_num is False:
                    positive_char = 1
                    continue
                else:
                    break

            elif ch.isdigit():
                if negative_char == 1:
                    result_str += "-" + ch
                    negative_char = 0
                else:
                    result_str += ch
                detect_num = True

            else:  # Case for any other characters
                if detect_num is True:
                    break
                else:
                    return 0  # Non-whitespace and "-" found before number

        # Convert resulting string to an intenger
        if result_str == "":
            return 0
        else:
            result_int = int(result_str)

        # Check for 32-bit INT overflow
        if result_int > MAX_INT:
            return MAX_INT
        elif result_int < MIN_INT:
            return MIN_INT
        else:
            return result_int


if __name__ == "__main__":
    runSolution = Solution()

    test_str = "42"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 42
    print("Passes: " + test_str)

    test_str = "    -42"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == -42
    print("Passes: " + test_str)

    test_str = "    - 42"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 0
    print("Passes: " + test_str)

    test_str = "    -a 42"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 0
    print("Passes: " + test_str)

    test_str = "4192 with Drew"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 4192
    print("Passes: " + test_str)

    test_str = "words and 123"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 0
    print("Passes: " + test_str)

    test_str = "-91283472332"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == -2**31
    print("Passes: " + test_str)

    test_str = "91283472332"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == (2**31) - 1
    print("Passes: " + test_str)

    test_str = ""
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 0
    print("Passes: " + test_str)

    test_str = "+1"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 1
    print("Passes: " + test_str)

    test_str = "+ 1"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 0
    print("Passes: " + test_str)

    test_str = "+a 1"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 0
    print("Passes: " + test_str)

    test_str = "+-2"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 0
    print("Passes: " + test_str)

    test_str = "-+2"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 0
    print("Passes: " + test_str)

    test_str = "--2"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 0
    print("Passes: " + test_str)

    test_str = "++2"
    my_int = runSolution.myAtoi(test_str)
    assert my_int == 0
    print("Passes: " + test_str)
