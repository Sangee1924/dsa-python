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

def merge(leftHead,rightHead):
    dummby = Node(-1)
    temp = dummby
    while(leftHead!=None and rightHead!=None):
        if leftHead.data <= rightHead.data:
            temp.next=leftHead
            temp=temp.next
            leftHead = leftHead.next
        else:
            temp.next=rightHead
            temp=temp.next
            rightHead=rightHead.next
    if leftHead:
        temp.next=leftHead
    else:
        temp.next=rightHead

    return dummby.next

def middle(head):
    slow=head
    fast=head.next
    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
    return slow

def sortLL(head):
    if (head==None or head.next==None):
        return head
    mid = middle(head)
    leftHead = head
    rightHead = mid.next
    mid.next=None
    leftHead = sortLL(leftHead)
    rightHead = sortLL(rightHead)

    return merge(leftHead,rightHead)

def main():
    arr=[5,4,3,2,1]
    head = convertArr2LL(arr)
    head = sortLL(head)
    element(head)

main()