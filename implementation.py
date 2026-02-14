def add(a,b):
    return a+b
def sub(c,d):
    return c-d
def mul(e,f):
    return e*f
def div(g,h):
    return g/h
print("==============================")
print("1.TO PERFORM ADDITION")
print("2.To PERFORM SUBTRACTION")
print("3.TO PERFOM MULTIPLICATION")
print("4.To PERFORM DIVISION")
print("5.EXIT")
print("=============================")
while True:
    choice=int(input("Enter your choice:"))
    if choice==1:
        a=int(input("Enter the 1st value:"))
        b=int(input("Enter the 2nd value:"))
        print(add(a,b))
    elif choice==2:
        c=int(input("Enter the 1st value:"))
        d=int(input("Enter the 2nd value:"))
        print(sub(c,d))
    elif choice==3:
         e=int(input("Enter the 1st value:"))
         f=int(input("Enter the 2nd value:"))
         print(mul(e,f))
    elif choice==4:
        g=int(input("Enter the 1st value:"))
        h=int(input("Enter the 2nd value:"))
        print(div(g,h))
    elif choice==5:
        print("Exited")
        break
    else:
        print("Wrong Choice")
