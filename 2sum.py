def two_sum(nums, target):

    # Loop through the list and create a dictionary
    key_dict = {}
    for idx, item in enumerate(nums):
        # the key is the number, the index is the value
        key_dict[item] = idx

    # Now for every item, see if the corresponding value
    # needed to hit the target is in the dictionary
    for idx, item in enumerate(nums):

        # Find the needed value to meet the target
        need_num = target - item

        # If the value is in the dictionary
        if need_num in key_dict.keys():
            # ensure we are not using the same index twice
            if key_dict[need_num] == idx:
                continue
            else:
                # return current index, and index of dictionary item
                return idx, key_dict[need_num]

    # No match found, return -1, -1
    return -1, -1


if __name__ == "__main__":
    str = "Basic Case 1"
    indexes = two_sum([2, 7, 11, 15], 9)
    assert indexes == (0, 1)
    print("Passes: " + str)

    str = "Idx (0,0) matches target"
    indexes = two_sum([3, 2, 4], 6)
    assert indexes == (1, 2)
    print("Passes: " + str)

    str = "No answer"
    indexes = two_sum([3, 2, 4], 8)
    assert indexes == (-1, -1)
    print("Passes: " + str)

    str = "One value is target"
    indexes = two_sum([8, 2, 4], 8)
    assert indexes == (-1, -1)
    print("Passes: " + str)

    str = "Duplicate Values"
    indexes = two_sum([5, 2, 5, 11], 10)
    assert indexes == (0, 2)
    print("Passes: " + str)
