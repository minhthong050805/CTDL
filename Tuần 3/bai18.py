class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
n1 = Node(1)
n2 = Node(3)
n3 = Node(2)
n1.next = n2
n2.next = n3
head = n1
swapped = True
while swapped:
    swapped = False
    cur = head
    while cur.next:
        if cur.val > cur.next.val:
            cur.val, cur.next.val = cur.next.val, cur.val
            swapped = True
        cur = cur.next
cur = head
result = []
while cur:
    result.append(cur.val)
    cur = cur.next
print(result) 
