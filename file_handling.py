                                                    ## file processing in python ##
## Things to be noted ##
# "r" - opens file for reading
# "w" - opens a file for writing
# "x" - creates a file if not exists
# "a" - append, add more content to a file
# "t" - text mode
# "b" - Binary mode
# "+" - read and write


my_file = open("fruits.txt")
print (my_file.readlines())
# print (my_file.read(1))
# print (my_file.read(1))
# print (my_file.read(1))
# print (my_file.read(1))

# my_file = open("bear.txt")
# print (my_file.read()[:91])

# def findi(charc, filepath):
#         file = open(filepath)
#         content = file.read()
#         return content.count(charc)

# print (findi('d', 'testi.txt'))