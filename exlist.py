#python code to try lists 
my_list = ["Sachin", "Sourav", "Dhoni", "Kumble"]

print(my_list)

#empty list

empty_list = []

print (empty_list)

#list with different data types

diff_list = ["text", 1, {"hello", 5}]

print(diff_list)

game_board = ["sachin", 100], ["sourav", 99]

print(game_board)

#converting iterables to list 

conv_list = ("ramu", "komu")

print(list(conv_list))

#can not convert non iterable will get error 

my_string = "hello"

print(list(my_string))

# below code will give error so commenting out as int is not iterable

#my_num = 10

#print(list(my_num))

#accessing elemets 

print (my_list[0])

#get last element in list 

print (my_list [-1])

multi_list = [1,2], [3,4], [5,6]

print (multi_list[0])

print (multi_list[0] [1])

print (multi_list[2] [0])

new_list = [1, 2]

new_list.append('Hello')

print(new_list)

#combine merge lists 

l1 = [1, 2]
l2 = [3, 4]

l3 = l1 + l2 

print (l3)

l1.extend(l2)

print(l1)

#pop removes items and return items 
#pop() without index retuns and removes last item

pop_list = [1, 2, 3, 4, 5]

p1 = pop_list.pop()

print(p1, pop_list)

p2 = pop_list.pop(3)

print(p2, pop_list)

#del can be used to delete list or element in list 

del_list = [1, 2, 3, 4, 5]

del(del_list[3])

print (del_list)

del(del_list)

#below will give error as del_list will not be available after above statement
#print (del_list)

rem_list = [1, 2, 3, 4, 5, 3]

rem_list.remove(3)

print(rem_list)

rem_list.remove(3)

print(rem_list)

#below will return error as there are no more 3 in list
#rem_list.remove(3)

#remove all clear all items from list 

clr_list = [1, 2, 3, 4]

clr_list.clear()

print(clr_list)

#removing duplicates from list 

dup_list = [1, 2, 2, 3, 4, 3]

non_dup = set(dup_list)

dup_list = list(non_dup)

print (non_dup)

#replace items 

rep_list = [1, 2, 3, 4]

rep_list[2] = 500

print(rep_list)

len1 = len(rep_list)

print (len1)

#counting occurance of element in list 

occ_list = [1, 2, 5, 2, 7, 2]

print(occ_list.count(2))

#check if an item is present in list

chk_item = [1, 2, 3, 4]

if 3 in chk_item:
    print("3 is in list")

#find index of an item in list 

list_idx = [1, 2, 3, 4, 5, 2]

idx = list_idx.index(2)

print(idx)

print (list_idx.index(2, 2))

my_list_new = [1, 2, 3, 4, 5, 4]

print(my_list_new.index(4, 4))

loop_list = [1, 2, "biju", 5]

for n in loop_list:
    print (n)

#sorting list

sort_list = [1, 2, 3, 5, 7, 0, 4]

sort_list.sort()

print (sort_list)

sort_list.sort(reverse=True)

print(sort_list)

#using sorted 

sorted_list = [1,0, 7, 9 , 2, 5]

ns_list = sorted(sorted_list)

print(sorted_list)
print(ns_list)

err_sort = [1, 'a', 2, 'b']

#below will give error as types are different

#err_sort.sort()

#print(err_sort)

#slicing 

slice_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(slice_list[0:3])

print(slice_list[:4])

print(slice_list[5:])

print(slice_list[::2])

print(slice_list[::-2])

print(slice_list[-1:-4:-2])

#reverse a python list 

rvrse = [1, 2, 3, 4]

rvrse.reverse()

print ("using list reverse " ,  rvrse)

rvrse.reverse()

rvrse2 = rvrse[::-1]

print(rvrse2)

lst1 = [1, 2, 3, 4, 5, 6]
rev = reversed(lst1)
print(rev)

for i in rev:
    print(i)
    



