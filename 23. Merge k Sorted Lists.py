# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Purge empty lists
        count = 0
        while count < len(lists):
            if lists[count] == None:
                lists.pop(count)
            else:
                count += 1
        
        # initiliaze dummy head
        head = ListNode()
        cur = head

        while len(lists) > 0:
            # Find current remaining min
            cur_min = 10000000
            cur_min_index = 0
            for i in range(len(lists)):
                if lists[i].val < cur_min:
                    cur_min = lists[i].val
                    cur_min_index = i
            # Add to final LL
            cur.next = lists[cur_min_index]
            cur = lists[cur_min_index]
            # Remove if end of list, else update next value to lists head
            if not lists[cur_min_index].next:
                lists.pop(cur_min_index)
            else:
                lists[cur_min_index] = cur.next
        return head.next
                
            