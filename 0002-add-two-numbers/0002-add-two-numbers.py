# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        list1 = list()
        list2 = list()
        current_2 = l2
        while current:
            list1.append(current.val)
            current = current.next
        while current_2:
            list2.append(current_2.val)
            current_2 = current_2.next
        print(list1, list2)
        list1.reverse()
        list2.reverse()
        print(list1, list2)
        number1 = ''.join(str(x) for x in list1)
        number2 = ''.join(str(x) for x in list2)
        print(number1, number2)
        
        answer = int(number1) + int(number2)
        print(answer)
        answer = str(answer)
        answer_node = ListNode()
        current_ans = answer_node
        for char in reversed(answer):
            current_ans.next = ListNode(int(char))
            current_ans = current_ans.next
        return answer_node.next
        

        