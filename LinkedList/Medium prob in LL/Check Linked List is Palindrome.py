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
        mover = temp
    return head

def reverse(head):
    if (head==None or head.next==None):
        return head
    newHead = reverse(head.next)
    front = head.next
    front.next=head
    head.next=None
    return newHead

def palindromeCheck(head):
    slow=head
    fast=head
    while(fast.next!=None and fast.next.next!=None):
        slow=slow.next
        fast=fast.next.next
    newHead=reverse(slow.next)
    left=head
    right=newHead
    while(right!=None):
        if left.data != right.data:
            reverse(newHead)
            return False
        left=left.next
        right=right.next
    reverse(newHead)
    return True

def main():
    arr=[1,2,3,2,1]
    head = convertArr2LL(arr)
    print(palindromeCheck(head))

main()