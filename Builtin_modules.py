import time
import os

# while True:
#     with open('vegetables.txt') as file:
#         print (file.read())
#         time.sleep(5)

            #### in the above code if we delete or move vegetables file program will stop
            #### to avoid that scenario we need to import another module os on the top
while True:
    if os.path.exists('vegetables.txt'):     ## this time even if the file is not there program will keep going ##
        with open('vegetables.txt') as file:
            print (file.read())
    else:
        print ("file doesn't exist")
    time.sleep(5)
