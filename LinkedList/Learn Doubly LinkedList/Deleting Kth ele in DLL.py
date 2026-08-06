class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.back=None
    def __str__(self):
        return str(self.data)

def convertArr2DLL(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        temp.back=prev
        prev.next=temp
        prev=temp
    return head

def element(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

def deleteHead(head):
    prev = head
    head=head.next
    head.back=None
    prev.next=None
    return head

def deleteTail(head):
    tail = head
    while (tail.next!=None):
        tail=tail.next
    prev = tail.back
    prev.next=None
    tail.back=None
    return head

def deleteKthNode(head,k):
    if head==None or k<=0:
        return head
    cnt=0
    temp=head
    while(temp!=None):
        cnt+=1
        if cnt==k:
            break
        temp=temp.next
    if temp==None:
        return head
    prev = temp.back
    front = temp.next
    if prev == None and front == None:
        return None
    elif prev == None:
        return deleteHead(head)
    elif front==None:
        return deleteTail(head)
    prev.next = front
    front.back=prev
    temp.next=None
    temp.back=None
    return head

def main():
    arr=[1,2,3,4,5]
    head = convertArr2DLL(arr)
    element(head)
    k = int(input("Enter Node to delete: "))
    head = deleteKthNode(head,k)
    element(head)

main()