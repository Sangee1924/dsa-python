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

def helper(head):
    if head == None:
        return 1
    carry = helper(head.next)
    head.data = head.data + carry
    if head.data < 10:
        return 0
    head.data = 0
    return 1

def Addone(head):
    carry = helper(head)
    if carry==1:
        newhead = Node(carry)
        newhead.next = head
        return newhead
    return head

def main():
    arr=[1,8,9,9]
    head = convertArr2LL(arr)
    element(head)
    head = Addone(head)
    element(head)

main()