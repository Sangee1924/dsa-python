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

def EvenOdd(head):
    if head==None or head.next==None:
        return head
    odd = head
    even = head.next
    evenHead = head.next
    while(even != None and even.next != None):
        odd.next = odd.next.next
        even.next = even.next.next

        odd=odd.next
        even=even.next
    odd.next=evenHead
    return head

def main():
    arr=[1,4,2,5,3]
    head = convertArr2LL(arr)
    head = EvenOdd(head)
    element(head)


main()