def insert(stack,temp):
    if not stack:
        stack.append(temp)
        return
    val = stack.pop()
    insert(stack,temp)
    stack.append(val)

def reverseStack(stack):
    if not stack:
        return
    temp = stack.pop()
    reverseStack(stack)
    insert(stack,temp)

stack = [1,2,3,4]

reverseStack(stack)
print(stack)