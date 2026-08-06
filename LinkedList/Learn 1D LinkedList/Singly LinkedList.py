class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)


def Ele(head):
    temp=head
    while(temp):
        print(temp.data,end=" ")
        temp=temp.next

def main(): 
    arr=[1,2,3,4]
    head = Node(arr[0])
    mover=head
    for i in range(1,len(arr)):
        temp=Node(arr[i])
        mover.next=temp
        mover=temp
    return head
head=main()
Ele(head)