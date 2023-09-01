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



