class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

def LinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    mover=head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next=temp
        mover=temp
    return head

def element(head):
    while(head is not None):
        print(head.data,end=" ")
        head=head.next
    print()

def deleteTail(head):
    if head is None or head.next is None:
        return None
    temp=head
    while temp.next.next != None:
        temp=temp.next
    temp.next=None
    return head

def main():
    arr=[1,2,3,4,5]
    head = LinkedList(arr)
    element(head)
    head = deleteTail(head)
    element(head)

main()