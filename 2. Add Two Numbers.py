class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Init cur pointer
        cur1 = l1
        cur2 = l2

        # Carry value to next digit
        carry = 0

        # Iterate through l1
        while cur1:
            # Add value from l2 and update value
            new_val = cur1.val + (cur2.val if cur2 else 0) + carry
            carry = new_val // 10
            cur1.val = new_val % 10


            if cur2:
                cur2 = cur2.next 

            has_more = cur2 or carry
            if not has_more:
                # Break out early, no more l2 or carry
                return l1
            elif not cur1.next and has_more:
                    # Add new node to root
                    cur1.next = ListNode()
            cur1 = cur1.next
        return l1