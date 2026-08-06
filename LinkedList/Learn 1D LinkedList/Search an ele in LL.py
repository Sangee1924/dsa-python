class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

def LinkedList(arr):
    head=Node(arr[0])
    mover=head
    for i in range(1,len(arr)):
        temp=Node(arr[i])
        mover.next=temp
        mover=temp
    return head

def search(head,searchElement):
    temp=head
    while(temp!=None):
        if temp.data==searchElement:
            return True
        temp=temp.next
    return False

def main():
    arr=[1,2,3,4,5]
    head = LinkedList(arr)
    s = int(input("Enter element to search: "))
    print(search(head,s))

main()