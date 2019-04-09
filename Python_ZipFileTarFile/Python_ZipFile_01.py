# The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, append, and list a ZIP file.
# It can handle ZIP files that use the ZIP64 extensions (that is ZIP files that are more than 4 GiB in size). It supports decryption of encrypted files in ZIP archives, but it currently cannot create an encrypted file.
# Decryption is extremely slow as it is implemented in native Python rather than C.
# zipfile模块用来做zip格式编码的压缩和解压缩的，zipfile里有两个非常重要的class, 分别是ZipFile和ZipInfo, 在绝大多数的情况下，我们只需要使用这两个class就可以了。
# ZipFile是主要的类，用来创建和读取zip文件而ZipInfo是存储的zip文件的每个文件的信息的。

# zipfile.write()
# zipfile.extract()
# zipfile.extractall()
# zipfile.namelist()

import zipfile
import os
import subprocess

print(os.sep)

# it is important to first change to the destination folder,
# if not, when decompressed, sub folders will be created under the destination decompression folder.
os.chdir("/home/nathan/")
# let's first create a zip file.

# if a zip file with the same name already exists, delete it

if os.path.exists("shutil.zip"):
    os.remove("shutil.zip")

# os.listdir(), list all items under a directory
output = os.listdir("/home/nathan/")
print(type(output))
print("****************************************")

# zipfile.ZipFle(), write method
zipped_file = zipfile.ZipFile("shutil.zip","w")

if os.path.isdir("shutil_dir/"):
    for i in os.listdir("shutil_dir/"):
        zipped_file.write(i)
    zipped_file.close()
# print(subprocess.call("ls -l /home/nathan/", shell=True))

# let's check if the zip file exists
if os.path.exists("/home/nathan/shutil.zip"):
    print("Compression Successful")


# decompress the zip file, using the read method
# ZipFile.extract(member[, path[, pwd]])
# 将zip文档内的指定文件解压到当前目录。参数member指定要解压的文件名称或对应的ZipInfo对象；参数path指定了解析文件保存的文件夹；参数pwd为解压密码。
# 下面一个例子将保存在程序根目录下的text.zip内的所有文件解压到/home/nathan/tst/：

print("************Decompressing a zip file*****************")

zipped_file2=zipfile.ZipFile("shutil.zip")
for file in zipped_file2.namelist():
    print(file)
    zipped_file2.extract(file, "/home/nathan/tst/")
    # equals zipped_file2.extractall("/home/nathan/tst/")
zipped_file2.close()


