# #we can apply regex and file handling to find something in a file
#there is a library which is useful called pathlib

my_file = open("C:/Users/RAJARAJAN JAYAKUMAR/Desktop/Sample.txt") # in here use / or \\ besided \ cause it cosider as a escape sequence
print(my_file)
# # or use raw sting literal
my_file = open(r"C:\Users\RAJARAJAN JAYAKUMAR\Desktop\Sample.txt")
print(my_file.read()) #read open and show the content inside the file, index by index and the cursor ends in last
print(my_file.read()) #you can only read the file only once
my_file.seek(0)# If i want to read the same file again, use seek(index value) here
print(my_file.read())

# #if you want to read next line, one command moves to next line only
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

# #if you want to read all lines, and it'll return list only
print(my_file.readlines())

# # to close the file
my_file.close()


# Read, Write, Append
# this is the standard way to read a file
with open("C:/Users/RAJARAJAN JAYAKUMAR/Desktop/Sample.txt", mode="r") as myfile: #in here mode='r' is read and if not specified its default
    print(myfile.read())
    print(myfile.readlines())
with open("C:/Users/RAJARAJAN JAYAKUMAR/Desktop/Sample.txt", mode="r+") as myfile: #To read and write mode = r+
    
    text = myfile.write('hey its me')
    print(text)# the output will be the length which is 10
with open("C:/Users/RAJARAJAN JAYAKUMAR/Desktop/Sample.txt", mode="a") as myfile: #To append mode = a
    
    text = myfile.write('hey its me and')
    print(text)# the output will be the length which is 10

# file I/O error, Try to use try except all time
try: 
    with open("C:/Users/RAJARAJAN JAYAKUMAR/Desktop/Sample.txt", mode="r") as myfile:
        print(myfile.read())
        print(myfile.readlines())
except FileNotFoundError as Filenotfounderror:
    print("file doesnt exist")
    raise Filenotfounderror
except IOError as ioerror: #when machine has some problem with read or write file 
    print("IO error")
    raise ioerror
