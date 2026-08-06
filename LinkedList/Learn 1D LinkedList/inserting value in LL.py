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
        temp = Node(arr[i])
        mover.next=temp
        mover=temp
    return head

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def Insertion(head,k,num):
    if head is None:
        return None
    
    temp=head
    while temp != None:
        if k == temp.data:
            insertion=Node(num)
            insertion.next=temp.next
            temp.next=insertion
            return head
        temp=temp.next
    
    return head

def main():
    arr=[1,2,3,4,5]
    head = linkedList(arr)
    k = int(input("Enter the insertion val: "))
    num = int(input("Enter value to insert: "))
    head = Insertion(head,k,num)
    element(head)

main()