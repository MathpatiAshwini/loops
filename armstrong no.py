a=int(input("enter the number:"))
b=a
sum=0
i=1
while b>0:
    digit=b%10
    b=b//10
    sum+=digit**3
if sum==a:
    print(a,"is armstrong no...")
else:
    print(a,"is not armstrong number...")