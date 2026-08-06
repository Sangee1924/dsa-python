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

def findKthnode(temp,k):
    k=k-1
    while(temp!=None and k>0):
        k-=1
        temp=temp.next
    return temp

def reverse(temp):
    if temp==None or temp.next==None:
        return temp
    newHead = reverse(temp.next)
    front = temp.next
    front.next = temp
    temp.next = None

    return newHead

def ReverseKGroup(head,k):
    temp = head
    prevnode = None
    while(temp!=None):
        kthNode = findKthnode(temp,k)
        if (kthNode==None):
            if (prevnode):
                prevnode.next=temp
                break   
            else:
                return head
            
        nextnode = kthNode.next
        kthNode.next=None

        newHead = reverse(temp)

        if temp == head:
            head = newHead
        else:
            if (prevnode):
                prevnode.next=newHead

        prevnode = temp
        temp=nextnode

    return head

def main():
    arr=[1,2,3,4,5]
    head = convertArr2LL(arr)
    element(head)
    k = int(input("Enter reverse Group Size: "))
    head = ReverseKGroup(head,k)
    element(head)

main()