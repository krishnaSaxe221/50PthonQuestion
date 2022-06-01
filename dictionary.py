n=int(input())
d={}
for i in range(n):
    key=input()
    value=int(input())
    d.update({key:value})
s=0
for i in d.values():
    s+=i
print(s)
n=int(input())
d={}
for i in range(n):
    key=input()
    value=int(input())
    d.update({key:value})
l=list(d.values())
l.sort()
print(l)
n=int(input())
d={}
for i in range(n):
    key=input()
    value=int(input())
    d.update({key:value})
n1=int(input())
d1={}
for i in range(n1):
    key=input()
    value=int(input())
    d1.update({key:value})
d.update(d1)
print(d)
n=int(input())
d={}
for i in range(n):
    key=input()
    value=int(input())
    d.update({key:value})
n1=int(input())
for i in d.values():
    if i==n1:
        print("number found")
        break
else:
    print("number not found")
n=int(input())
d={}
for i in range(n):
    key=int(input())
    value=int(input())
    d.update({key:value})
p=1
for i in d.values():
    p*=i
for i in d.keys():
    p*=i
print(p)
n=int(input())
d={}
for i in range(1,n+1):
    d.update({i:i*n})
print(d)
