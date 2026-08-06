class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.back=None
    def __str__(self):
        return str(self.data)

def convertArr2DLL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        temp.back=prev
        prev.next=temp
        prev=temp
    return head

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def insert(head,val,temp):
    if head is None or temp is None:
        return head
    prev= temp.back
    new = Node(val)
    new.next=temp
    temp.back=new

    if prev is None:
        return new

    prev.next=new
    new.back=prev

    return head

def main():
    arr=[1,2,3,4,5]
    head = convertArr2DLL(arr)
    element(head)
    val = int(input("Enter Insertion value : "))
    head = insert(head,val,head.next)
    element(head)

main()