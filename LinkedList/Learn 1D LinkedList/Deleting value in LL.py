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
    mover = head
    for i in range(1,len(arr)):
        temp=Node(arr[i])
        mover.next=temp
        mover=temp
    return head

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print() 

def deleteVal(head,val):
    if head is None:
        return None
    if head.data == val:
        return head.next
    temp = head
    prev = None
    while temp is not None:
        if temp.data == val:
            prev.next=temp.next
            break
        prev=temp
        temp=temp.next
    return head

def main():
    arr=[1,2,3,4,5]
    head = LinkedList(arr)
    val = int(input("Enter the value to delete: "))
    head = deleteVal(head,val)
    element(head)

main()