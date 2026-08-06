class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.back=None
    def __str__(self):
        return str(self.data)

def convertArr2DLL(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        temp.back=prev
        prev.next=temp
        prev=temp
    return head

def reverse(head):
    if head is None or head.next is None:
        return head
    temp = head
    last=None
    while(temp != None):
        last=temp.back
        temp.back=temp.next
        temp.next=last
        temp=temp.back
    return last.back

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def main():
    arr=[1,2,3,4,5]
    head = convertArr2DLL(arr)
    element(head)
    head = reverse(head)
    element(head)

main()