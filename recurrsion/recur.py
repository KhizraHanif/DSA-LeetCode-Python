# recurrsion is a process in which fucntion calls itsself until a specific condition met 
## that condition is call basecase.   without basecase function will keep calling itslf and it will cause stack overflow and will casue memory error  
count = 0

def fuc():
    global count

    if count >= 5:
        return

    count = count + 1
    print(count)
    fuc()

fuc()


def fic(n):
    if n == 0:
        return 1

    return n* fic(n-1)

ffic = fic(5)

print(ffic)



