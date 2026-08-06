class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

def ConvertArr2LL(arr):
    head = Node(arr[0])
    mover = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover=temp
    return head

def middle(head):
    slow=fast=head
    while(fast != None and fast.next != None):
        slow=slow.next
        fast=fast.next.next
    return slow

def main():
    arr=[1,2,3,4,5]
    head = ConvertArr2LL(arr)
    mid = middle(head)
    print("Middle element in a Linked List :",mid)

main()