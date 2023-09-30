import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="python",
  password="3110"
)

mycursor = mydb.cursor()


mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)












