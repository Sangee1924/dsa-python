class ListNode:
    def __init__(self, data=0, next=None, child=None):
        self.data = data
        self.next = next
        self.child = child

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.child
    print()

def merge(list1,list2):
    dummy = ListNode()
    temp = dummy
    while(list1!=None and list2!=None):
        if list1.data <= list2.data:
            temp.child=list1
            temp = list1
            temp.next=None
            list1=list1.child
        else:
            temp.child=list2
            temp=list2
            temp.next=None
            list2=list2.child
    if list1:
        temp.child=list1
    else:
        temp.child=list2

    dummy.next=None
    return dummy.child

def Flattening(head):
    if head==None or head.next==None:
        return head
    head2 = Flattening(head.next)

    return merge(head,head2)


def main():    
    # Create a linked list with child pointers
    head = ListNode(5)
    head.child = ListNode(14)

    head.next = ListNode(6)
    head.next.child = ListNode(10)

    head.next.next = ListNode(7)
    head.next.next.child = ListNode(11)
    head.next.next.child.child = ListNode(12)

    head.next.next.next = ListNode(8)
    head.next.next.next.child = ListNode(17)
    head = Flattening(head)
    element(head)

main()