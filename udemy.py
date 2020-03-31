# x= (list(range(0,10)))

# student_grades = [9.1, 8.8, 7.5]
# max_value = max(student_grades)
# print (max_value)


# student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
# highest = student_grades.count(10.0)
# print (highest)

# username = "Python3"
# x = username.lower()
# print (x)


# student_grades = {"ibrahim" : 9.1 ,"fehan" : 8.8, "afaf" : 7.5}
# mysum = sum(student_grades.values())
# length = len(student_grades)
# mean = mysum / length
# print (mean)
# print (student_grades.values()) # to print only values from an item
# print (student_grades.keys())   # to print only keys from an item




# day_temperatures = {'morning': (10.1,11.1,12.3) , 'noon': (11.1,22.2,33.3) , 'evening': (44.4,55.5,66.6)}



# seconds = [1.2323442655, 1.4534345567, 1.023458894]
# current = 1.10001399445
# seconds.append(current)
# print (seconds)


# seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
# seconds.remove(1.4534345567)
# seconds.remove(1.023458894)
# seconds.remove(1.10001399445)
# print(seconds)



# atif = ['Afaf', 'Kulsoom', 'Aleen', 'Ibrahim']
# firstbaby = atif.__getitem__(0) 
# firstbaby = atif[0]
# print (firstbaby)


# workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# weekend = ["Sat", "Sun"]
# workdays.append(weekend[0])
# print (workdays)


                                    # Defining own function in python #
# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)         # this function gives output of average value of a list
#     return the_mean

# x = (22,33,44,11,55)
# print (mean[33,22,44,11])
# print (mean(x))

# print (type(mean))  # a function created by me.


                        # my function to check length of string #
# def lambi(x):
#     return len(x)
# print (lambi("atif"))



# def foo(oz):
#     return oz * 29.57353
# print (foo(5))

                           # Defining a function to get average value of list as well as dictionary. smart function

def avrg(value):
    if type(value) == dict:
        the_avrg = sum(value.values()) / len(value)
    else:
        the_avrg = sum(value) / len(value)
    return the_avrg


                            ## this is another example to write this code in using true #
def avrg(value):
    if isinstance(value, dict):
        the_avrg = sum(value.values()) / len(value)
    else:
        the_avrg = sum(value) / len(value)
    return the_avrg


                        # these lines for testing above conditional function #
# student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
# student_grades = {"ibrahim" : 9.1 ,"fehan" : 8.8, "afaf" : 7.5}
# print (avrg(student_grades))
# print (sum(student_grades.values()) / len(student_grades))
# print (type(student_grades))


            ## this function from udemy quiz for practice #
# def foo(x, array):
#     if x in array:
#         return True
#     else:
#         return False
 
# print(foo(1, [1, 2, 3]))
# print(foo(1, [2, 3]))
# print(foo(1, ['1', 2, 3]))

                        # defining a function exercise in udemy #
# def foo(value):
#     if len(value) < 8:
#         return False
#     else:
#         return True

# print (foo("mylongpass"))


                        # defining a function exercise in udemy for if else conditions #

# def chktmp(tmp):
#     if tmp > 7 :
#         return "Warm"
#     else:
#         return "cold"

# print (chktmp(5))

                        # defining a function with elif #

# def chktmp(tmp):
#     if tmp > 25:
#         return "Hot"
#     elif tmp >= 15 and tmp <= 25:
#         return "Warm"
#     else:
#         return "Cold"

# print (chktmp(14))


# message = "1 2 3 4 5 6"
# if "3" in message:
#     print ("hi")
# else:
#     print ("i don't \nknow")

            # my function #
# def foo(name):
#     return "Hi %s" %(name)

# print (foo('atif'))

            # my function #
# def foo(name):
#     return "Hi %s" %(name).capitalize()

# print (foo("afaf"))



# a = "ibrahim"
# b = "atif"
# c = "khan"

# z = "hi my sweet daughter %s %s %s" %(a, b, c)
# print (z)


# colors = [11, 34, 98, 43, 45, 54, 54]
# for x in colors:
#     print (x)

# colors = [11, 34, 98, 43, 45, 54, 54]
# for x in colors:
#     if x > 50:
#         print (x)

# colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
# for x in colors:
#     if type(x) == int:
#         print (x)


# colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
# for x in colors:
#     if type(x) == int and x > 50:
#         print (x)

                    # for loop with own defined function #
# def celsius_to_kelvin(cels):
#     return cels + 273.15

# monday_temperatures = [9.1, 8.8, -270.15]
 
# for temperature in monday_temperatures:
#     print(celsius_to_kelvin(temperature))

#             # for loop for dictionaries #
# cars_dict = {'atif':'sonata', 'asim':'cultus', 'salman':'honda'}
# print (cars_dict['atif'])               # this line is for testing
# for x in cars_dict.items():             # replace .items with keys and values to get correspondings output #
#     print (x)


                        # Bonus code of dictionary loop and string formatting #
# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

# for car in cars_dict.items():
#     print("{} has as {} car".format(car[0], car[1]))

# for key, value in cars_dict.items():
#     print("{} has as phone number {}".format(key, value))    

                        # exercise for loop and string formatting #
# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# for nam, numb in phone_numbers.items():
#     print("%s: %s" % (nam, numb))

# You could make use of the str.replace(char1, char2) method for this. It replaces char1 with char2 in the string.

# for value in phone_numbers.values():
#     print(value.replace('+','00'))

# x = ("my name is khan")        # this is for practice #
# print(x.replace("khan","atif"))

                # while loop quiz #

# a = 10
# while a > 0:
#     x = a + 1
#     print(x)

# a = 0
# while a < 5:
#     a = a + 1
#     print(a)

                    # while loop with Break & Continue #

# x = input('set usernsame! ')
# y = input('set password! ')

# while True:
#     username, password = input("please enter username and password with space ! ").split(" ")
#     if username == x and password == y:
#         break
#     else:
#         continue


while True:
    x = input('Say something')
    print (x.capitalize())
    if x == "\\end":
        break
    else:
        continue