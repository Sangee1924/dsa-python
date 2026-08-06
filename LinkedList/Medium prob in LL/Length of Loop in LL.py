class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

def Looplength(head):
    slow=head
    fast=head
    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
        if fast == slow:
            fast=fast.next
            cnt=1
            while fast!=slow:
                cnt+=1
                fast=fast.next
            return cnt
    return None

def main():
    head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)
    fifth = Node(5)

    head.next=second
    second.next=third
    third.next=forth
    forth.next=fifth

    fifth.next=third

    print(Looplength(head))

main()