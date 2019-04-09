import platform
import os
import time


########################################################################################
# Use the platform module to get information about the operating system itself
########################################################################################
print("############################Get operating system information#########################################")
# Get the type of the operating system
print(platform.system())

if platform.system() == 'Linux':
    print("You are using the " + platform.system() + " operating system")

if platform.system() == "Windows":
    print("You are using Windows")
elif platform.system() == "Linux":
    print("You are using Linux")


print(platform.version())
print(platform.platform())

print("###############################Test the version of Python######################################")
# Get the version of Python
print(platform.python_version())

# To judge which Python version is being used
if platform.python_version()[0] == "2":
    print("You are using a lower version of Python, please use a higher version")
else:
    print("It seems you are using the right Python version")


# Define a function
def get_platform():
    return platform.platform()

print(get_platform())




#####################################################################
# How to use the os module, create a file, verify if a file exists
# os.path.exist()
# os.makedirs()
# os.removedirs()
#####################################################################
print("############################Create files#########################################")
linux_files=["/home/nathan/opt/test/a.log","/home/nathan/opt/test/b.log","/home/nathan/opt/test/c.blog"]
for file in linux_files:
    if os.path.exists(file):
        print("Step 1: After checking, found " + file + " already exists, " + time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Step 2: Deleting " + file +" ..., " + time.strftime("%Y-%m-%d %H:%M:%S"))
        os.removedirs(file)
        print("Step 3: " + file + " already deleted, " + time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Step 4: Recreating file " + file + " ..., " + time.strftime("%Y-%m-%d %H:%M:%S"))
        os.makedirs(file)
        print("Step 5: File already created!" + time.strftime("%Y-%m-%d %H:%M:%S"))
        print("***********************************")
    else:
        print("Step 1: After checking, found " + file + " doesn't exist, " + time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Step 2: Creating file " + file + " ..., " + time.strftime("%Y-%m-%d %H:%M:%S"))
        os.makedirs(file)
        print("Step 3: " +file + " already created!" + time.strftime("%Y-%m-%d %H:%M:%S"))
        print("***********************************")