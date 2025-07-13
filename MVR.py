# cook your dish here
a,b,x,y=map(int,input().split())
messi=(2*a)+b
ronaldo=(2*x)+y  
if(messi>ronaldo):
    print("Messi")
elif(ronaldo>messi):
    print("Ronaldo")
else:
    print("Equal")