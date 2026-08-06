class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.back=None
    def __str__(self):
        return str(self.data)

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def convertArr2DLL(arr):
    head = Node(arr[0])
    mover = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next=temp
        temp.back=mover
        mover=temp
    return head

def DeleteAllKey(head,key):
    temp = head
    while temp!=None:
        nextTemp = temp.next
        if temp.data==key:
            if temp==head:
                head=head.next
            nextnode = temp.next
            pervnode = temp.back
            if nextnode:
                nextnode.back=pervnode
            if pervnode:
                pervnode.next=nextnode
            temp.next=None
            temp.back=None
        temp=nextTemp
    return head

def main():
    arr=[1,2,3,4,1,5]
    head = convertArr2DLL(arr)
    element(head)
    key = int(input("Enter key to Delete: "))
    head = DeleteAllKey(head,key)
    element(head)


main()