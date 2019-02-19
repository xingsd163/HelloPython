# how to read/write a file

# os.remove(), delete a file
# os.rmdir(), deletes a directory
# os.path.exists()
# Create an empty file: f = open('/home/nathan/nonexist.log', 'w')


import os
import os.path

print("*********************************************************************************")
print("Detect whether a file exists, remove it if yes, and then create a new empty file")
print("*********************************************************************************")

try:
    os.remove('/home/nathan/nonexist.log')
    f=open('/home/nathan/nonexist.log', 'r')
except FileNotFoundError:
    print('File not found, please try again.')
finally:
    print('Creating file ...')
    # Create an empty file
    f = open('/home/nathan/nonexist.log', 'w')
    if os.path.exists('/home/nathan/nonexist.log'):
        print("File exists")

print("*********************************************************************************")
print("Write to a file -01")
print("*********************************************************************************")

# the best practice is to use With

with open('/home/nathan/write_file','a') as f:
    f.write('Hello World')
    f.close()
    print("Write done")

with open('/home/nathan/write_file', 'r') as f:
    print(f.read())



print("*********************************************************************************")
print("Write to a file -02")
print("*********************************************************************************")

# the best practice is to use With
if os.path.exists('/home/nathan/write_file'):
    print("File exists, deleting ...")
    os.remove('/home/nathan/write_file')

# Use /n to break line
with open('/home/nathan/write_file','a') as f:
    f.write('Hello World\n')
    f.write("Hello Python\n")

    f.close()
    print("Write done")

with open('/home/nathan/write_file', 'r') as f:
    #print("f.read(): " + f.read())
    #print("f.readlines(): " + str(f.readlines()))
    for i in str(f.readlines()).split(','):
        print(i)
    f.close()


print("*********************************************************************************")
print("Write to file - 03 - Appending")
print("*********************************************************************************")


# if file not exists, create a new file
# if use 'w', the old file will be overwritten
# if use 'a', the new lines will be appended to old files.

with open('/home/nathan/test02.log','a') as test002:
    test002.write('First line\n')
    test002.write('Second line\n')
    test002.write('Third line')
    test002.close()

# read a file line by line
print("*********************************************************************************")
print("Write to file - 04 - Read by line")
print("*********************************************************************************")

with open('/home/nathan/test02.log','r') as test002:
    for line in test002:
        print(line)
    test002.close()

# read a file line by line
print("*********************************************************************************")
print("Write to file - 05 - Read by line")
print("*********************************************************************************")

with open('/home/nathan/test02.log', 'r') as test002:
    for line in test002.readlines():
        print(line.strip())
    test002.close()


