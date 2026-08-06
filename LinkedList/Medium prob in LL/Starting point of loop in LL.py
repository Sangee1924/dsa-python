class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

def cycleStating(head):
    slow=head
    fast=head    
    while (fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
        if slow == fast:
            slow=head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next
            return slow
    return None

def main():
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third
    print(cycleStating(head))

main()