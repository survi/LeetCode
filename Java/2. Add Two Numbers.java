/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l3 = null, l4 = null;
        int l = 0, m = 0, n = 0, sum = 0;


        do{
            
            sum = (l1!=null?l1.val:0) + (l2!=null?l2.val:0) + n;
            if (sum >= 10){
                n = 1;
                sum -= 10;
            }else{
                n = 0;
            }
            if ( m == 0){
                l3 = new ListNode(sum);
                l4 = l3;
                m++;
            }else{
                l3.next = new ListNode(sum);
                l3 = l3.next;
            }
            
            l1 = (l1!=null?l1.next:null);
            l2 = (l2!=null?l2.next:null);
        }while(l1 != null || l2!= null);
        if (n == 1){
            l3.next = new ListNode(1);
        }

        return l4;
    }
}