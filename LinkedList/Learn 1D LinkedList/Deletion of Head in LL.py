class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)
    
def linkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    mover=head
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

def DeletionOfHead(head):
    if head is None:
        return None
    head=head.next
    return head

def main():
    arr=[1,2,3,4,5]
    # Creating Linked List
    head = linkedList(arr)
    # Printing the Original Linked List Elements
    element(head)
    # Deleting the head of the Linked List
    head = DeletionOfHead(head)
    # Printing Linked List after Deleting the Head
    element(head)

main()