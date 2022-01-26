package H;

import java.lang.Math;
import java.util.ArrayList;

class Solution {
    public static void main(String[] args) {
        Solution mySol = new Solution();
        System.out.println("hhhh");
        System.out.println(mySol.addTwoNumbers(make_list(999999),make_list(9999)).val);
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode cur_node1 = l1;
        ListNode cur_node2 = l2;    
        ArrayList<Integer> output = new ArrayList<Integer>();
        int carry = 0;

        while ((cur_node1!=null) && (cur_node2!=null)) {
            int sum = cur_node1.val + cur_node2.val + carry;
            carry = Math.max(0,sum-10); 
            output.add(sum % 10);

            cur_node1 = cur_node1.next;
            cur_node2 = cur_node2.next;
        }

        // Woo add the rest
        while (cur_node1!=null) {
            int sum = (cur_node1.val)+carry;
            output.add(sum%10);
            carry = Math.max(0,sum-10);
            cur_node1 = cur_node1.next;
        }

        while (cur_node2!=null) {
            int sum = (cur_node2.val%10)+carry;
            output.add(sum%10);
            carry = Math.max(0,sum-10);
            cur_node2 = cur_node2.next;
            carry = 0;
        }

        System.out.println(output);
        return l1;
    }

    public static ListNode make_list(int val) {
        String[] my_vals = String.valueOf(val).split("");
        ListNode root = null;
        ListNode prev = null;

        for(String character : my_vals) {
            root = new ListNode(Integer.parseInt(character),prev); 
            prev = root;
        }

        return root;
    }
}

