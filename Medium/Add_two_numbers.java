package Medium;

// Definition for singly-linked list.
class Add_two_numbers {
    class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode result = new ListNode(0);
        ListNode pointer = result;

        while (l1 != null || l2 != null || carry > 0) {
            int l1Val = 0;
            int l2Val = 0;
            if (l1 != null) {
                l1Val = l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                l2Val = l2.val;
                l2 = l2.next;
            }

            ListNode temp = new ListNode((l1Val + l2Val + carry) % 10);
            carry = (l1Val + l2Val + carry) / 10;
            pointer.next = temp;
            pointer = pointer.next;
        }
        result = result.next;
        return result;
    }
}
