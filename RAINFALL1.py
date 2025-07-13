# cook your dish here
t=int(input())
for _ in range(t):
    x=int(input())
    if(x<3):
        print("Light")
    elif(x>=3 and x<7):
        print("Moderate")
    else:
        print("Heavy")