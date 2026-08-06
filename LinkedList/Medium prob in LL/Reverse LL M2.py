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

def reverse(head):
    if head == None or head.next==None:
        return head
    newHead = reverse(head.next)
    front = head.next
    front.next=head
    head.next=None
    return newHead

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def main():
    arr=[1,2,3,4,5]
    head = ConvertArr2LL(arr)
    head = reverse(head)
    element(head)
main()