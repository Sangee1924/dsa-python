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

def tail(head):
    while(head.next!=None):
        head=head.next
    return head

def SumPairs(head,SUM):
    left = head
    right = tail(head)
    dl=[]
    while (left != right and left.back != right):
        if left.data + right.data == SUM:
            dl.append([left.data,right.data])
            left=left.next
            right=right.back
        elif left.data + right.data < SUM:
            left=left.next
        else:
            right=right.back
    return dl

def main():
    arr=[1,2,3,4,5]
    head = convertArr2DLL(arr)
    element(head)
    SUM = int(input("Enter key to Delete: "))
    print(SumPairs(head,SUM))
    
main()