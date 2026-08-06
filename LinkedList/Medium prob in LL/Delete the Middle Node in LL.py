class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

def convertArr2LL(arr):
    head = Node(arr[0])
    mover = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next=temp
        mover=temp
    return head

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def deleteMiddle(head):
    if head==None or head.next==None:
        return None
    slow=head
    fast=head
    fast=fast.next.next
    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
    middle= slow.next
    slow.next=slow.next.next
    middle.next=None
    return head

def main():
    arr=[1,2,3,4,5]
    head = convertArr2LL(arr)
    head = deleteMiddle(head)
    element(head)

main()