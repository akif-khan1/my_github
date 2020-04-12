# import datetime
# print (datetime.datetime.now())

                ## list comprehension practice ##


# def organizer(*args):
#     new_list = []
#     return ((args.upper()).append(new_list))


                ## udemy exercise ##

        ## defining a function for unlimited arguments of strigs and returns a list of strings in upper case and sorted. ##

# def foo(*args):
#     args = [x.upper() for x in args]
#     return sorted(args)

# print (foo('snow', 'glacier', 'iceburg')) 

            ## Defining a function with a keyword argument for unlimited arbitary numbers##

# def mean(**kwargs):
#     return(kwargs)

# print (mean(a=1, b=2, c=3)) ## output will be a dictionary with keys and values ##

# def find_sum(**kwargs):
#     return sum(kwargs.values())
    
# print(find_sum(a=9))

#### An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:

# def find_max(*args):
#     return max(args)
# print(find_max(3, 99, 1001, 2, 8))


#### An **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:

# def find_winner(**kwargs):
#     return max(kwargs, key = kwargs.get)
 
# print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))

# def mean(**kwargs):
#         return kwargs

# print (mean(a=1,b=2,c=3))