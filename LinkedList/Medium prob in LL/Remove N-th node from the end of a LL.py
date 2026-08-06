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
        mover = temp
    return head

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def remove(head,N):
    slow=head
    fast=head
    while N>0:
        fast=fast.next
        N-=1
    if fast is None:
        return head.next
    while(fast.next!=None):
        slow=slow.next
        fast=fast.next

    front = slow.next
    slow.next=slow.next.next
    front.next=None

    return head

def main():
    arr=[1,2,3,4,5]
    head = convertArr2LL(arr)
    N = int(input("Enter Node to remove: "))
    head = remove(head,N)
    element(head)

main()