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

def lambi(x):
    return len(x)

# print (lambi("atif"))

def foo(oz):
    return oz * 29.57353

# print (foo(5))

                           # Defining a function to get average value of list as well as dictionary. smart function

def avrg(value):
    if type(value) == dict:
        avrg = sum(value.values()) / len(value)
    else:
        avrg = sum(value) / len(value)
    return avrg


# student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
student_grades = {"ibrahim" : 9.1 ,"fehan" : 8.8, "afaf" : 7.5}
print (avrg(student_grades))
# print (sum(student_grades.values()) / len(student_grades))
# print (type(student_grades))