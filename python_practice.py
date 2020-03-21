                 # login program #
x = input('please set your username! ')
y = input('please set your password! ')
print('\nuser and pass has been set \n\n        please login! ')

# a = False
b = "tea"

while (b=="tea"):
    username = input('\nplease enter your username: ')
    password = input('please enter your password: ')

    if username == x and password == y:
        b = "cofee"
        print('\nwelcome to my first login program!')
    else:
        b = "tea"
        print ('\nFailed! enter username and password again')

print('\nOk, you are done')

# x , y = (input('please input two numbers comma seperated ').split(','))
# x = int(x)
# y = int(y)



                    #*practice*#
# a= False

# while a==False:
#     x , y = (input('please input two numbers comma seperated ').split(','))
#     x = int(x)
#     y = int(y)
#     if (x+y)<=100:
#         print (x+y)
#         a=True
#     else:
#         print ('sum of two num is greater than 100')
#         a=False

# print ("good luck")