import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input('Enter a word to translate!\n')    ## Actual program line

# query = cursor.execute("SELECT * FROM Dictionary")
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " %word)               ## Actual program line
# query = cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE 'r%' ")
# query = cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE 'rain%' ")
# query = cursor.execute("SELECT * FROM Dictionary WHERE length(Expression) < 4")
# query = cursor.execute("SELECT * FROM Dictionary WHERE length(Expression) = 4")
# query = cursor.execute("SELECT * FROM Dictionary WHERE length(Expression) > 1 AND length(Expression) < 4")
# query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression  LIKE 'r%'")

results = cursor.fetchall()

# print (results)
# print (resutls[0])


if results:                                       ## Actual program line
    for result in results:
        print (result[1])
else:
    print ('No words found!')