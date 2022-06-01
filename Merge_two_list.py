def merge(list1,list2):
    merge=list1+list2
    merge.sort()
    return merge
list1=[1,2,3,4]
list2=[3,4,5,6]
print("The first list is:")
print(list1)
print("The second list is:")
print(list2)
v=merge(list1,list2)
print(v)
