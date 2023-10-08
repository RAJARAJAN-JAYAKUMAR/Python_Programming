'''Consider the file test.txt and perform following operations
1. open the file if exists, if not create  a new file
2. add string 'abcde' to the end of the file
3. read and display first 5 characters
4. display total number of characters present in the file'''
try:
    file = open(r"C:\Users\RAJARAJAN JAYAKUMAR\Desktop\Python\Sample.txt", mode = 'a')
except FileNotFoundError as fd:
    file = open(r"C:\Users\RAJARAJAN JAYAKUMAR\Desktop\Python\Sample.txt", mode = 'w') 

file.write('abcde')   
file.close

file = open(r"C:\Users\RAJARAJAN JAYAKUMAR\Desktop\Python\Sample.txt", mode = 'r')
print(file.read())
first_five = file.read(5)
print("first five char:",first_five)

file.seek(0)
file_contents = file.read()
total_char = len(file_contents)
print("Total no of characters:",total_char )




















