import random



"""class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#linked list generator
size = random.randint(4,9)
connection = random.randint(1,size-1)
linked_list = []
pos1 = 0
pos2 = 1

for x in range(size):
    linked_list.append(x)

print(linked_list, "Connected at " + str(connection))

next_node = None
root = ListNode(linked_list[size-1])
start = None
connected_node = None

for x in reversed(range(size)):
    new_node = ListNode(x)

    if x == (size-1):
        print("root",new_node.val)
    else:
        if x == 0:
            start = new_node
            start.next = next_node
        if x == connection:
            root.next = new_node
            connected_node = new_node
            new_node.next = next_node
        else:
            new_node.next = next_node
    next_node = new_node

def print_linked(start):
    x = 0
    start = start
    while(x!= 20):
        print(start.val)
        if start.next != None:
            start = start.next
        else:
            print(start.val, root.val, start.val, start.next, root.next.val)
        x+=1

print("asdasd",root.val,root.next.val, connected_node)
print_linked(start)"""