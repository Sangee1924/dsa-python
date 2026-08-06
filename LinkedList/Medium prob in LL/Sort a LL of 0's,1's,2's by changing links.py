class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

def convertArr2LL(arr):
    head = Node(arr[0])
    mover = head
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

def sortLL(head):
    zerohead = Node(-1)
    oneHead = Node(-1)
    twoHead = Node(-1)
    zero = zerohead
    one = oneHead
    two = twoHead
    temp = head
    while(temp!=None):
        if temp.data == 0:
            zero.next = temp
            zero=temp
        elif temp.data == 1:
            one.next = temp
            one=temp
        else:
            two.next=temp
            two=temp
        temp=temp.next

    zero.next = oneHead.next if oneHead.next else twoHead.next
    one.next = twoHead.next
    two.next = None

    return zerohead.next

def main():
    arr=[1,2,0,0,2,1]
    head = convertArr2LL(arr)
    head = sortLL(head)
    element(head)

main()