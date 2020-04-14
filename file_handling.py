                                                    ## file processing in python ##
## Things to be noted ##
# "r" - opens file for reading
# "w" - opens a file for writing
# "x" - creates a file if not exists
# "a" - append, add more content to a file
# "t" - text mode
# "b" - Binary mode
# "+" - read and write

                ## open a file to read ##
# my_file = open("fruits.txt")
# print (my_file.read())

# content = my_file.read()
# my_file.close()
# print (content)

# def findi(charc, filepath):
#         file = open(filepath)
#         content = file.read()
#         return content.count(charc)

# print (findi('m', 'fruits.txt'))


            ## another way of reading a file ##
# with open("fruits.txt") as my_file:
#     content = my_file.read()

# print (content)

                ## open function creates a new file and write some text into it with 'w' mode ##

# with open('vegetables.txt', 'w') as my_file:      # "w" mode overwrite the file with new content
#     my_file.write('tomato\nonions\npotato')

                ## now we learn to open a file in 'a' append mode to add some text not overwrite 

# with open('vegetables.txt', 'a+') as my_file:          ## + with a means append with read and write mode. if + removed file will not be read.
#     my_file.write('\ngarlic')
#     my_file.seek(0)                                    ## seek method used to put the cursor back on to 0 position.
#     content = my_file.read()
#     my_file.close()                                    ## file must be closed to free up the resources.
# print (content * 3)
