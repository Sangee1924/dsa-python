class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

def LinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    mover = head
    for i in range(1,len(arr)):
        temp=Node(arr[i])
        mover.next=temp
        mover=temp
    return head

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print() 

def delete(head,k):
    if k<=0:
        return head
    if head is None:
        return None
    if k==1:
        return head.next
    cnt=1
    temp = head
    prev=None
    while temp is not None:
        if cnt==k:
            prev.next=temp.next
            break
        cnt+=1
        prev = temp
        temp=temp.next
    return head

def main():
    arr=[1,2,3,4,5]
    head = LinkedList(arr)
    k = int(input("Enter the Position to delete: "))
    head = delete(head,k)
    element(head)

main()