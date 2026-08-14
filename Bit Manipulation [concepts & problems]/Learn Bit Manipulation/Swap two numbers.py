def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b


a= int(input("Enter an Number :"))
b= int(input("Enter an Number :"))
print(f"a = {a}, b = {b}")
a,b = swap(a,b)
print(f"a = {a}, b = {b}")