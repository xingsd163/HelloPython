import os
import os.path

# os.getcwd(), 返回当前工作目录
# os.listdir(path):列举目录下的所有文件。返回的是列表类型。
# os.path.abspath(path):返回path的绝对路径。
# os.path.split(path):将路径分解为(文件夹,文件名)，返回的是元组类型。可以看出，若路径字符串最后一个字符是\,则只有文件夹部分有值；若路径字符串中均无\,则只有文件名部分有值。若路径字符串有\，且不在最后，则文件夹和文件名均有值。且返回的文件夹的结果不包含\.
# os.path.join(path1,path2,...):将path进行组合，若其中有绝对路径，则之前的path将被删除。
# os.path.dirname(path):返回path中的文件夹部分，结果不包含'\'
# os.path.basename(path):返回path中的文件名。
# 查看文件时间
#  os.path.getmtime(path):文件或文件夹的最后修改时间，从新纪元到访问时的秒数。
#  os.path.getatime(path):文件或文件夹的最后访问时间，从新纪元到访问时的秒数。
#  os.path.getctime(path):文件或文件夹的创建时间，从新纪元到访问时的秒数。
# os.path.getsize(path): 文件或文件夹的大小
# os.path.exists(path):文件或文件夹是否存在，返回True 或 False。
# os.remove(path)	删除文件路径。
# os.removedirs(path)	递归删除目录。
# os.rename(src, dst)	将文件或目录src重命名为dst。
# os.rmdir(path), 删除目录路径
# os.chdir(path)	将当前工作目录更改为指定路径。
# os.chmod(path, mode)	将路径模式更改为数字模式。
# os.chown(path, uid, gid)	将指定的路径的所有者和组ID更改为数字uid和gid。
# os.chroot(path)	将当前进程的根目录更改为指定的路径。
# os.environ()
# os.getenv()

# https://www.cnblogs.com/yufeihlf/p/6179547.html


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

# Get environmental variables

print(os.environ)