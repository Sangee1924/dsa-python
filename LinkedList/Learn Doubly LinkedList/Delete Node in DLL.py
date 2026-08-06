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
def DeleteHeadNode(head):
    prev=head
    head=head.next
    head.back=None
    prev.next=None
    return head

def DeleteTailNode(head,node):
    prev=node.back
    prev.next=None
    node.back=None
    return head

def deleteNode(head,node):
    if head is None or node is None:
        return head
    prev = node.back
    front = node.next
    if prev == None and front == None:
            return None
    elif front is None:
        return DeleteTailNode(head,node)
    elif prev is None:
        return DeleteHeadNode(head)
    prev.next=front
    front.back=prev
    node.next=None
    node.back=None
    return head

def main():
    arr=[1,2,3,4,5]
    head = convertArr2DLL(arr)
    element(head)
    head = deleteNode(head,head.next.next)
    element(head)


main()