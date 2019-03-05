# https://www.cnblogs.com/wf-linux/archive/2018/08/01/9400354.html

# The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal.
# For operations on individual files, see also the os module.

# os.rename(), 重命名
# os.path.getsize()
# os.listdir()

# shutil.copy()
# shutil.move()
# shutil.rmtree()
# Delete an entire directory tree; path must point to a directory
# shutil.copytree()

# Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order, and does not include the special entries '.' and '..' even if they are present in the directory.
# shutil.disk_usage()
# Return disk usage statistics about the given path as a named tuple with the attributes total, used and free, which are the amount of total, used and free space, in bytes.


import shutil
import subprocess
import os

if os.path.exists('/home/nathan/Downloads/dnf.log'):
    os.remove('/home/nathan/Downloads/dnf.log')

shutil.copy('/home/nathan/dnf.log','/home/nathan/Downloads')
print("O1: ",subprocess.getstatusoutput('ls -l /home/nathan/Downloads')[1])

# use shutil.rmtree() because the folder is not empty
# if the folder is empty, os.removedirs() can be used
# 判断文件夹是否为空，如果为空，可以使用os.removedirs() 删除文件夹；
# 如果不为空，则需要使用shutil.rmtree()来删除文件夹

if not len(os.listdir('/home/nathan/shutil_dir/')) == 0:
    print('Folder is not empty, printing files in this folder...')
    for i in os.listdir('/home/nathan/shutil_dir/'):
        print("File name: " + i)
        print("The size of this file is " +str(os.path.getsize("/home/nathan/shutil_dir/" + i)) + " bytes")

print("******************This is another world!**********************")

if os.path.exists("/home/nathan/shutil_dir/"):
    shutil.rmtree("/home/nathan/shutil_dir/")

if os.path.exists('/home/nathan/shutil_dir/dnf.log'):
    os.remove('/home/nathan/shutil_dir/dnf.log')

os.mkdir('/home/nathan/shutil_dir')
shutil.move('/home/nathan/Downloads/dnf.log','/home/nathan/shutil_dir')

print("02: ",subprocess.getstatusoutput('ls -l /home/nathan/shutil_dir')[1])


print("****************************Disk usage************************************")
# print("Disk Usage: ",shutil.disk_usage("/home/nathan/"))
disk_usage = shutil.disk_usage("/home/nathan/")
print(disk_usage)
print(type(disk_usage))

total,used,free=shutil.disk_usage("/home/nathan/")
print("Total: " + str(total/1024/1204/1024) + " GB")
print("Used: " + str(used/1024/1204/1024) + " GB")
print("Free: " + str(free/1024/1204/1024) + " GB")


# shutil.copytree()
# Recursively copy an entire directory tree rooted at src, returning the destination directory. The destination directory, named by dst, must not already exist;

print("****************************shutl.copytree()************************************")

print('Step 1: deleting /home/nathan/Documents/Downloads/ if it exists ...')
if os.path.exists("/home/nathan/Documents/Downloads/"):
    shutil.rmtree("/home/nathan/Documents/Downloads/")

print('Step 2: copying /home/nathan/Downloads/ to /home/nathan/Documents/Downloads/ ...')
shutil.copytree("/home/nathan/Downloads/","/home/nathan/Documents/Downloads/")

print('Step 3: verifying and found',os.listdir('/home/nathan/Documents/Downloads/'))