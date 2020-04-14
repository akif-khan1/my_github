import time
import os
import pandas


while True:
    if os.path.exists('temps_today.csv'):     
        data = pandas.read_csv('temps_today.csv')
        print (data.mean())
        # print (data.mean()['st1'])    # if we need mean of only st1 column #
    else:
        print ("file doesn't exist")
    time.sleep(5)