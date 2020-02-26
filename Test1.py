# List1=['atif', 'shafiq', 'khan']
# List1.append ('usman')
# print (List1*2)

# Tupple1= ('atif', 'shafiq', 'khan')
# print (Tupple1[2])

# print ('Hello, Welcome to my game.')
# x=input ('Please type your name ')
# print ('Welcome ' + x)
# x=input('what is your year of birth? ')
# print ('you will be ' + str(2020-int(x)) + ' years old next year.')


# #list in python, list can have text nums anything, list can be added into another list or can be multiplied but can't be divide or subtracted! #
# nums=[1,2,3,4]
# strs=['atif', 'shafiq']
# mylist=[nums, strs]
# print (mylist)

# list1=['atif', 'shafiq']
# print (list1)
# list1.append('khan')
# print (list1)

# num=[1,2,3,4,5,6,7,8]
# del num [2]
# num[2] =11
# print(num)  # deleting an item from list

# in mapping we use only {}, mapping has a key and its value.#
# car_list={'atif':'sonata', 'asim':'cultus', 'fehan':'blue','ibrahim':'red bike'}
# in mapping has key and its corresponding value.
# car_list['fehan'] = 'blue bike'  # changing value of the key, but key itself can't be changed.
# print(car_list)

# del car_list['fehan'] # Deleting a key from list
# print (car_list)

# car_list['atif']='Accord' #another example of changing value.
# print(car_list)

# map1 = {'atif':'sonata','asim':'accord','fehan':'blue bike'}
# map1['atif']='accord 2017'
# map1['asim'] = 'accord2020'
# if 'fehan' not in map1.keys():
#     map1['fehan'] = 'red bike'
# print (map1)


# username = input('enter your username ')
# password = input('enter your password ')

# if username == 'admin' and password == '123':
#     print('welcome!')
# else:
#     print ('invalid username or password!')



                 # login program #
# x = input('please set your username! ')
# y = input('please set your password! ')
# print('user and pass has been set \nplease login! ')

# # a = False
# b = "tea"

# while (b=="tea"):
#     username = input('please enter your username: ')
#     password = input('please enter your password: ')

#     if username == x and password == y:
#         b = "cofee"
#         print('welcome!')
#     else:
#         b = "tea"
#         print ('incorrect!')

# print('Ok, you are done')


                            # while loop #
# i = 9
# while i <= 10:
#     print(f'hello world {i}')
#     i = i + 1


# total = 0
# i = 1
# while i <= 10:
#     total = total + i     # total += i
#     i = i + 1             # i += 1
# print (total)



n = int(input('enter a number: '))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print (total)


# a="atif shafiq khan"
# print (len(a))

# number = input('enter a number more than 1 digit: ')
# total = 0
# i = 0
# while i < len(number):
#     total += int(number[i])
#     i += 1
# print (total)


# a =  "aatiaf"
# b=a.count(a)
# print(b)


            # Nested if else #

# winning_number = 27
# user_input = input('guess a number b/w 1 and 100 :')
# user_input = int(user_input)
# if user_input == winning_number:
#     print ('you win!')
# else:
#     if user_input < winning_number:
#         print('too low')
#     else:
#         print('too high')