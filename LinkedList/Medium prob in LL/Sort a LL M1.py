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

def merge(num,low,mid,high):
    left=low
    right=mid+1
    temp=[]
    while(left<=mid and right<=high):
        if num[left] <= num[right]:
            temp.append(num[left])
            left+=1
        else:
            temp.append(num[right])
            right+=1
    while(left<=mid):
        temp.append(num[left])
        left+=1
    while(right<=high):
        temp.append(num[right])
        right+=1
    for i in range(len(temp)):
        num[low+i]=temp[i]

def MergeSort(num,low,high):
    if low>=high:
        return
    mid = (low+high)//2
    MergeSort(num,low,mid)
    MergeSort(num,mid+1,high)
    merge(num,low,mid,high)

def sortLL(head):
    temp=head
    num=[]
    while(temp!=None):
        num.append(temp.data)
        temp=temp.next
    Sortnum = MergeSort(num,0,len(num)-1)
    temp =head
    i=0
    while(temp!=None):
        temp.data=num[i]
        i+=1
        temp=temp.next
    return head

def main():
    arr=[1,2,3,4,1,5,1,3]
    head = convertArr2LL(arr)
    head = sortLL(head)
    element(head)

main()