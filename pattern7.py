# k=1
# i=1
# while k<=5:
#     j=1
#     while j<=k:
#         print(i,end=" ")
#         i=i+1
#         j=j+1
#     k=k+1
#     print()




print("welcome to State bank of india")
p=int(input("enter your 4 digit pin number:"))
m=25000
if(p==1234):
   print("1=withdraw")
   print("2=balance enquiry")
   print("3=fast cash")
   c=int(input("please choose transaction"))
   if(c==1):
