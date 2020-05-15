import time
from datetime import datetime as dt

host_temp    = r"D:\Python\Udemy\App3\hosts" # demo file in same directory
hosts_path   = r"C:\Windows\System32\drivers\etc\hosts"
redirect     = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "b4uglobal.com",]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 7) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print ('Working hours....')
        with open(host_temp, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " +website+"\n")
    else:
        with open(host_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print ("fun time....")
    time.sleep(5)
