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

def RemoveDuplicates(head):
    temp = head
    while temp:
        nexttemp=temp
        while(nexttemp.next!=None and nexttemp.data==nexttemp.next.data):
            nexttemp=nexttemp.next
        temp.next = nexttemp.next
        if nexttemp.next:
            nexttemp.next.back = temp
        temp=nexttemp.next
    return head

def main():
    arr=[1,1,1,2,3,3,4]
    head = convertArr2DLL(arr)
    element(head)
    head = RemoveDuplicates(head)
    element(head)
    
main()