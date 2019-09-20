class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None

a1 = Node(1)
a2 = Node(3)
a3 = Node(7)
a_head = Node()
a_head.next = a1
a1.next = a2
a2.next = a3

b1 = Node(2)
b2 = Node(4)
b3 = Node(6)
b_head = Node()
b_head.next = b1
b1.next = b2
b2.next = b3

def link_list_merge(a_head, b_head):
    pc = a_head
    pa = a_head.next
    pb = b_head.next
    while pa and pb:
    	if pa.value <= pb.value:
    		pc.next = pa
    		pc = pa
    		pa = pa.next
    	else:
    		pc.next = pb
    		pc = pb
    		pb = pb.next

    p = a_head.next
    while p:
    	print(p.value)
    	p = p.next

link_list_merge()