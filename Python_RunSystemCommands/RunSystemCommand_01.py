# Using Python 3+, there are several commands to run a system command:
# os.system()
# os.popen()
# Using the subprocess module

# os module - operating system interfaces
# This module provides a portable way of using operating system dependent functionality.
# If you just want to read or write a file see open(),
# if you want to manipulate paths, see the os.path module,
# and if you want to read all the lines in all the files on the command line see the fileinput module.
# For creating temporary files and directories see the tempfile module,
# and for high-level file and directory handling see the shutil module.

# os module
# os.path module
# fileinput module
# tempfile module
# shutil module

# https://www.cnblogs.com/clarenceyang/p/9811785.html


import os
import platform as pl


print(os.name)
print(pl.uname())
print(pl.version())

# os.getcwd()
# os.chdir()

print(os.getcwd())
print("Changing current working directory\n", os.chdir("/home/nathan"))
print(os.getcwd())

print("testing os.mkdir() and os.rmdir()")

print(os.path.exists("/home/nathan/mkdir_test01"))

# How to use not!!!!!
if not os.path.exists("/home/nathan/mkdir_test01"):
    os.mkdir("/home/nathan/mkdir_test01")
    print(os.path.exists("/home/nathan/mkdir_test01"))
else:
    os.removedirs("/home/nathan/mkdir_test01")

# True OR False, AND-OR-NOT
# True and False should be in upper case
# and or not should be in lower case
print("Using AND-OR-NOT")
print(True)
print(False)
print("and: ",True and False)
print("or: ", True or False)
print("not: ", not True)
print("not: ", not False)


if not os.path.exists("/home/nathan/sdfsdfs"):
    os.mkdir("/home/nathan/sdfsdfs")
    os.rmdir("/home/nathan/sdfsdfs")


# os.rename()


print(os.environ)
# os.system()
# os.system(command)
# Execute the command (a string) in a subshell. This is implemented by calling the Standard C function system(), and has the same limitations.
# On Unix, the return value is the exit status of the process encoded in the format specified for wait().
# The subprocess module provides more powerful facilities for spawning new processes and retrieving their results; using that module is preferable to using this function.

print(os.system("ls -a | grep test"))
print(os.system("ps -a | grep python"))


a=os.system("ps -a | grep python")
print(a)
print(type(a))

# It’s not a recommended way to use os.system() to execute shell commands. We will use Python subprocess module to execute system commands.


print("**************************************************")

import subprocess

# returns the exit code in unix
returned_value=subprocess.call("git --version", shell=True)
print(returned_value)

# Manipulate the output
# Using subprocess.check_output() function, we can store the output in a variable

cmd = "date"
returned_value2=subprocess.check_output(cmd)
print(returned_value2)
# decode()
print(returned_value2.decode("utf-8"))



# https://www.cnblogs.com/clarenceyang/p/9811785.html



