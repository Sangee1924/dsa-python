class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

def linkedList(arr):
    head=Node(arr[0])
    mover = head
    for i in range(1,len(arr)):
        temp=Node(arr[i])
        mover.next=temp
        mover=temp
    return head

def length(head):
    cnt=0
    while(head):
        cnt+=1
        head=head.next
    print(cnt)

def main():
    arr=[1,2,3,4,5]
    head = linkedList(arr)
    length(head)

main()