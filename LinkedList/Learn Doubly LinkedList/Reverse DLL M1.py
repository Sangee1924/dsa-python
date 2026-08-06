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

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def reverse(head):
    if head is None or head.next is None:
        return head
    temp = head
    stack=[]
    while temp:
        stack.append(temp.data)
        temp=temp.next
    temp = head
    while temp:
        temp.data=stack.pop()
        temp=temp.next

    return head

def main():
    arr=[1,2,3,4,5]
    head = convertArr2DLL(arr)
    element(head)
    head = reverse(head)
    element(head)

main()