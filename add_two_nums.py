# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    # Check for empty val - assuming both lists are the same length
    value = l1.val + l2.val
    carryover = 0

    # Check for "rollover"
    if value > 9:
        value = value % 10
        carryover = 1

    # If both lists are empty, at the base case
    if (l1.next is None) and (l2.next is None):
        return_list = ListNode(value)

    # Need more recursion
    else:
        # Left side empty
        if l1.next is None:
            # Add the carry over value as a single node to left side
            l1_next = ListNode(carryover)
            # Recurse!
            return_list = ListNode(value, addTwoNumbers(l1_next, l2.next))

        # Right side empty
        elif l2.next is None:
            # Add the carry over value as a single node to the right side
            l2_next = ListNode(carryover)
            # Recurse!
            return_list = ListNode(value, addTwoNumbers(l1.next, l2_next))

        # Both Lists non-empty
        else:
            # Add the carry over value to the first list
            l1_next = l1.next
            l1_next.val = l1_next.val + carryover
            # Recurse!
            return_list = ListNode(value, addTwoNumbers(l1_next, l2.next))

    return return_list


if __name__ == "__main__":
    # Test Cases
    # Basic test no rollovers, same length
    # Explanation: 343 + 455 = 798.
    l1 = ListNode(3)
    l1 = ListNode(4, l1)
    l1 = ListNode(3, l1)

    l2 = ListNode(5)
    l2 = ListNode(5, l2)
    l2 = ListNode(4, l2)

    test_str = "No Rollovers - same length"
    answer = addTwoNumbers(l1, l2)
    assert answer.val == 7
    answer = answer.next
    assert answer.val == 9
    answer = answer.next
    assert answer.val == 8
    print("Passes: " + test_str)

    # Rollovers, but same length
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    # Explanation: 342 + 465 = 807.
    l1 = ListNode(2)
    l1 = ListNode(4, l1)
    l1 = ListNode(3, l1)

    l2 = ListNode(5)
    l2 = ListNode(6, l2)
    l2 = ListNode(4, l2)

    test_str = "Rollovers - same length"
    answer = addTwoNumbers(l1, l2)
    assert answer.val == 7
    answer = answer.next
    assert answer.val == 0
    answer = answer.next
    assert answer.val == 8
    print("Passes: " + test_str)

    # No rollovers, different length
    # 200 + 455 = 655
    l1 = ListNode(2)

    l2 = ListNode(5)
    l2 = ListNode(5, l2)
    l2 = ListNode(4, l2)

    test_str = "No Rollovers - different length"
    answer = addTwoNumbers(l1, l2)
    assert answer.val == 6
    answer = answer.next
    assert answer.val == 5
    answer = answer.next
    assert answer.val == 5
    print("Passes: " + test_str)

    # Rollovers and different length
    # 900 + 455 = 1355
    l1 = ListNode(9)

    l2 = ListNode(5)
    l2 = ListNode(5, l2)
    l2 = ListNode(4, l2)

    test_str = "No Rollovers - different length"
    answer = addTwoNumbers(l1, l2)
    assert answer.val == 1
    answer = answer.next
    assert answer.val == 3
    answer = answer.next
    assert answer.val == 5
    answer = answer.next
    assert answer.val == 5
    print("Passes: " + test_str)