class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def clone(head):
    temp = head
    while(temp!=None):
        newnode = Node(temp.data)
        newnode.next=temp.next
        temp.next = newnode
        temp=temp.next.next
    temp = head
    while(temp!=None):
        temp.next.random = temp.random.next if temp.random else None
        temp=temp.next.next
    temp = head
    dummy = Node(-1)
    mover = dummy
    while(temp!=None):
        copy = temp.next
        mover.next=copy
        mover=mover.next

        temp.next=copy.next
        temp=temp.next

    return dummy.next

def main():
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    # Assigning random pointers
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next
    head.next.next.next.random = head.next

    head = clone(head)
    element(head)

main()