class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

def convertArr2LL(arr):
    head=Node(arr[0])
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

def Rotation(head,k):
    tail=head
    len=1
    while(tail.next!=None):
        len+=1
        tail=tail.next
    tail.next=head
    k=k%len
    N = len-k
    temp=head
    N=N-1
    while(temp!=None and N>0):
        N-=1
        temp=temp.next
    head = temp.next
    temp.next=None

    return head

def main():
    arr=[1,2,3,4,5]
    head = convertArr2LL(arr)
    element(head)
    k=int(input("Enter Rotation: "))
    head = Rotation(head,k)
    element(head)

main()