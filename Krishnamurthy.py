a=int(input())
g=a
fact=1
sum=0
while(a>0):
     r=a%10
     fact=1
     for i in range(1,r+1):
         fact=fact*i
     sum=sum+fact
     a=a//10
if(sum==g):
 print("Krishnamurthy Number")
else:
    print('not')
