def insert(stack,temp):
    if not stack or stack[-1]>=temp:
        stack.append(temp)
        return

    val = stack.pop()
    insert(stack,temp)

    stack.append(val)
    return stack

def sortStack(stack):
     if stack:
          temp = stack.pop()
          sortStack(stack)
          insert(stack,temp)

stack=[1,2,3,4]

sortStack(stack)
print(stack)