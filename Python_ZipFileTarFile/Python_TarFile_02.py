# Python自带的tarfile模块可以方便读取tar归档文件，可以处理使用gzip和bz2压缩归档文件tar.gz和tar.bz2
# 与tarfile对应的是zipfile模块，zipfile是处理zip压缩的

# tarfile.open()
# tarfile.add()
# tarfile.extract()

import tarfile
import os

os.chdir("/home/nathan/")

# firstly, let's create the first tar file
if os.path.exists('first.tar'):
    os.remove('first.tar')
with tarfile.open("first.tar", "w") as tar:
    tar.add("audit.log", arcname="audit.log")
if os.path.exists('first.tar'):
    print('Tar file created successfully')

# secondly, let's create the second tar.gz file
if os.path.exists('first.tar.gz'):
    os.remove('first.tar.gz')
with tarfile.open("first.tar.gz", "w") as tar:
    tar.add("audit.log", arcname="audit.log")
if os.path.exists('first.tar'):
    print('Tar.gz file created successfully')