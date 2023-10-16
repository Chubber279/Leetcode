import java.io.*;
import java.lang.*;
import java.util.*;

public class Reverse_linked_list {

    // Definition for singly-linked list.
    public class ListNode {
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

    public ListNode reverseList(ListNode head) {
        List<ListNode> listNodes = new ArrayList<>(null);
        ListNode pointer = head;

        while (pointer.next != null) {
            listNodes.add(pointer);
            pointer = pointer.next;

        }
        ListNode newHead = pointer;
        while (listNodes.size() > 0) {
            ListNode temp = listNodes.get(listNodes.size() - 1);
            System.out.println(temp.val);
            pointer.next = temp;
            pointer = temp;
        }
        return newHead;
    }

    public ListNode reverseListRecursive(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode pointer = reverseList(head.next);
        head.next.next = head;
        head.next = null;

        return pointer;
    }
}
