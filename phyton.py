list1 = [1,2,1]
list2 =[3,4,5]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 ==list1):
    print("List1 is a palindrome")
else:
    print("List1 is not a palindrome")