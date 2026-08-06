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

def AddTwoNum(head1,head2):
    dummy = Node(-1)
    temp = dummy
    carry=0
    while(head1!=None or head2!=None or carry):
        Sum=0
        if head1!=None:
            Sum+=head1.data
            head1=head1.next
        if head2!=None:
            Sum+=head2.data
            head2=head2.next
        Sum+=carry
        if Sum < 10:
            carry = 0
            node = Node(Sum)
            temp.next=node
            temp=temp.next
        else:
            carry = Sum//10
            node = Node(Sum%10)
            temp.next = node
            temp=temp.next
    return dummy.next

def main():
    arr1 = [9,9,9,9,9,9,9]
    arr2 = [9,9,9,9]
    head1 = convertArr2LL(arr1)
    element(head1)
    head2 = convertArr2LL(arr2)
    element(head2)
    head = AddTwoNum(head1,head2)
    element(head)

main()