def operations(num,target):
    temp=[]

    def rec(ind,total,prev,expre):
        if ind==len(num):
            if total==target:
                temp.append(expre)
            return

        for i in range(ind,len(num)):

            if i > ind and num[ind] == "0":
                break

            current_str = num[ind:i+1]
            current = int(current_str)

            if ind==0:
                rec(i+1,current,current,current_str)
            else:
                #"+"
                rec(
                    i+1,
                    total+current,
                    current,
                    expre + "+" + current_str
                )
                #"-"
                rec(
                    i+1,
                    total-current,
                    -current,
                    expre + "-" + current_str
                )
                #"*"
                rec(
                    i+1,
                    total - prev + prev * current,
                    prev*current,
                    expre + "*" + current_str
                )
        return

    rec(0,0,0,"")

    return temp

def main():
    num = "123"
    target = 6
    print(operations(num,target))


main()