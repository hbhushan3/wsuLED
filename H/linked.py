# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        roots = [l1,l2]
        nums = ["", ""]
        final_val = 0

        for pos, root in enumerate(roots):
            while root!=None:
                nums[pos]=str(root.val)+nums[pos]

                root=root.next

        for num in nums:
            print(num)
            final_val += int(num)
            print(final_val)

        return make_linked_list(final_val)


    def make_linked_list(self,numbers):
    #numbers is string
        prev_node = None

        for x in str(numbers):
            cur_node = ListNode(x,prev_node)
            prev_node = cur_node
        return cur_node

def print_nodes(root):
    while(root!=None):
        print(root.val)
        root = root.next


def make_linked_list(numbers):
    #numbers is string
    prev_node = None

    for x in str(numbers):
        cur_node = ListNode(int(x),prev_node)
        prev_node = cur_node
    return cur_node

l1 = make_linked_list("342")
l2 = make_linked_list("465")

#print_nodes(l1)
#print_nodes(l2)

obj = Solution
print_nodes(obj.addTwoNumbers(obj,l1,l2))