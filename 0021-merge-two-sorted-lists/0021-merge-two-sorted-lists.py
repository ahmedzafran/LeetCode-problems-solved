# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final_list= list()
        current = [list1, list2]
        for i in range(len(current)):
            while current[i]:
                #print(current[i].val)
                final_list.append(current[i].val)
                current[i] = current[i].next
        
        unformatted_ans = sorted(final_list)
        #print(unformatted_ans)
        if len(unformatted_ans) > 0:
            answer = ListNode(unformatted_ans[0])
            current = answer
        else:
            return None
        for i in range(len(unformatted_ans)):
            try:
                current.next = ListNode(unformatted_ans[i+1])
                current = current.next
            except IndexError:
                #current = answer
                #while current is not None:
                    #print(current.val)
                    #current = current.next
                return answer

            

