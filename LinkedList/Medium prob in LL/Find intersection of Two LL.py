class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

def insertNode(head, val):
    newNode = Node(val)
    if not head:
        head = newNode
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def insersection(head1,head2):
    t1=head1
    t2=head2
    while(t1!=t2):
        t1=t1.next
        t2=t2.next
        if (t1==t2):
            return t1
        if t1==None:
            t1=head2
        if t2==None:
            t2=head1
    return t1
   
def main():
    head = Node(1)
    insertNode(head, 3)
    insertNode(head, 1)
    insertNode(head, 2)
    insertNode(head, 4)
    head1 = head
    head = head.next.next.next  # Intersection point
    headSec = Node(3)
    head2 = headSec
    headSec.next = head
    print(insersection(head1,head2))


main()