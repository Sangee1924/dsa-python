class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.back=None
    def __str__(self):
        return str(self.data)

def ConvertArr2DLL(arr):
    head = Node(arr[0])
    prev=head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        prev.next=temp
        temp.back=prev
        prev=temp
    return head

def delete(head):
    if head==None or head.next==None:
        return None
    prev = head
    head=head.next
    head.back=None
    prev.next=None
    return head

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def main():
    arr=[1,2,3,4,5]
    head = ConvertArr2DLL(arr)
    element(head)
    head = delete(head)
    element(head)

main()