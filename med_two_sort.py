class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Empty array to hold values
        new_list = []

        # Get the median index
        len_1 = len(nums1)
        len_2 = len(nums2)
        total_len = len_1 + len_2

        # Get the median index
        if total_len % 2:  # odd number
            odd_num = 1
            idx1 = int((total_len - 1) / 2)
            idx2 = idx1
        else:  # even number
            odd_num = 0
            idx1 = int((total_len - 1) / 2)
            idx2 = int((total_len + 1) / 2)

        # Read the arrays until we reach idx1 and idx2
        for i in range(idx2 + 1):
            if len(nums1) == 0:
                if i == idx1 or i == idx2:  # Only save target indexes
                    new_list.append(nums2[0])
                nums2.pop(0)

            elif len(nums2) == 0:
                if i == idx1 or i == idx2:  # Only save target indexes
                    new_list.append(nums1[0])
                nums1.pop(0)

            else:
                if i == idx1 or i == idx2:  # Only save target indexes
                    new_list.append(min(nums1[0], nums2[0]))

                # Remove min value
                if nums1[0] < nums2[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)

        # Calculate the overall median
        if odd_num == 1:
            median_result = new_list[0]
        else:
            median_result = (new_list[0] + new_list[1]) / 2

        # Return the median
        return median_result


if __name__ == "__main__":
    runSolution = Solution()

    test_str = "Test 1"
    median_ans = runSolution.findMedianSortedArrays([1, 3], [2])
    assert median_ans == 2.0
    print("Passes: " + test_str)

    test_str = "Test 2"
    median_ans = runSolution.findMedianSortedArrays([1, 2], [3, 4])
    assert median_ans == 2.5
    print("Passes: " + test_str)
