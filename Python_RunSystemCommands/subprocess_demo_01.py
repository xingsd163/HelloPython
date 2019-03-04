# # https://www.cnblogs.com/wf-linux/archive/2018/08/01/9400354.html
# subprocess是Python 2.4中新增的一个模块，它允许你生成新的进程，连接到它们的 input/output/error 管道，并获取它们的返回（状态）码。这个模块的目的在于替换几个旧的模块和方法，如：
# os.system
# os.spawn*

# subprocess模块中的常用函数
#
# subprocess.run()	Python 3.5中新增的函数。执行指定的命令，等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例。
# subprocess.call()	执行指定的命令，返回命令执行状态，其功能类似于os.system(cmd)。
# subprocess.check_call()	Python 2.5中新增的函数。 执行指定的命令，如果执行成功则返回状态码，否则抛出异常。其功能等价于subprocess.run(..., check=True)。
# subprocess.check_output()	Python 2.7中新增的的函数。执行指定的命令，如果执行状态码为0则返回命令执行结果，否则抛出异常。
# subprocess.getoutput(cmd)	接收字符串格式的命令，执行命令并返回执行结果，其功能类似于os.popen(cmd).read()和commands.getoutput(cmd)。
# subprocess.getstatusoutput(cmd)	执行cmd命令，返回一个元组(命令执行状态, 命令执行结果输出)，其功能类似于commands.getstatusoutput()。

# 说明：
#
# 在Python 3.5之后的版本中，官方文档中提倡通过subprocess.run()函数替代其他函数来使用subproccess模块的功能；
# 在Python 3.5之前的版本中，我们可以通过subprocess.call()，subprocess.getoutput()等上面列出的其他函数来使用subprocess模块的功能；
# subprocess.run()、subprocess.call()、subprocess.check_call()和subprocess.check_output()都是通过对subprocess.Popen的封装来实现的高级函数，因此如果我们需要更复杂功能时，可以通过subprocess.Popen来完成。
# subprocess.getoutput()和subprocess.getstatusoutput()函数是来自Python 2.x的commands模块的两个遗留函数。它们隐式的调用系统shell，并且不保证其他函数所具有的安全性和异常处理的一致性。另外，它们从Python 3.3.4开始才支持Windows平台。

# 函数参数列表：
# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, universal_newlines=False)
#
# subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
#
# subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
#
# subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False, timeout=None)
#
# subprocess.getstatusoutput(cmd)
#
# subprocess.getoutput(cmd)

# 参数说明：
# args： 要执行的shell命令，默认应该是一个字符串序列，如['df', '-Th']或('df', '-Th')，也可以是一个字符串，如'df -Th'，但是此时需要把shell参数的值置为True。
# shell： 如果shell为True，那么指定的命令将通过shell执行。如果我们需要访问某些shell的特性，如管道、文件名通配符、环境变量扩展功能，这将是非常有用的。当然，python本身也提供了许多类似shell的特性的实现，如glob、fnmatch、os.walk()、os.path.expandvars()、os.expanduser()和shutil等。
# check： 如果check参数的值是True，且执行命令的进程以非0状态码退出，则会抛出一个CalledProcessError的异常，且该异常对象会包含 参数、退出状态码、以及stdout和stderr(如果它们有被捕获的话)。
# stdout, stderr：
# run()函数默认不会捕获命令执行结果的正常输出和错误输出，如果我们向获取这些内容需要传递subprocess.PIPE，然后可以通过返回的CompletedProcess类实例的stdout和stderr属性或捕获相应的内容；
# call()和check_call()函数返回的是命令执行的状态码，而不是CompletedProcess类实例，所以对于它们而言，stdout和stderr不适合赋值为subprocess.PIPE；
# check_output()函数默认就会返回命令执行结果，所以不用设置stdout的值，如果我们希望在结果中捕获错误信息，可以执行stderr=subprocess.STDOUT。
# input： 该参数是传递给Popen.communicate()，通常该参数的值必须是一个字节序列，如果universal_newlines=True，则其值应该是一个字符串。
# universal_newlines： 该参数影响的是输入与输出的数据格式，比如它的值默认为False，此时stdout和stderr的输出是字节序列；当该参数的值设置为True时，stdout和stderr的输出是字符串。
#

# subprocess.CompletedProcess类介绍
#
# subprocess.run()函数是Python3.5中新增的一个高级函数，其返回值是一个subprocess.CompletedPorcess类的实例，因此，subprocess.completedPorcess类也是Python 3.5中才存在的。它表示的是一个已结束进程的状态信息

import subprocess


print("***********************subprocess.run()***************************")
print(subprocess.run(["pwd"]))
print(subprocess.run(["ls","-l"]))

result = subprocess.run(["pwd"])
print(type(result))

print(subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE))

# 如果shell为True，那么指定的命令将通过shell执行。如果我们需要访问某些shell的特性，如管道、文件名通配符、环境变量扩展功能，这将是非常有用的
print("#############shell=True##############")
print(subprocess.run('ls -l',shell=True))


print("***********************subprocess.call()***************************")

print(subprocess.call(['ls','-l']))
result1=subprocess.call(['ls','-l'])
# subprocess.call()	执行指定的命令，返回命令执行状态
print(type(result1))
print(result1)

print("#############shell=True##############")
print(subprocess.call('ls -l',shell=True))




print("***********************subprocess.check_call()***************************")

print(subprocess.check_call(['ls','-l']))
result2=subprocess.check_call(['ls','-l'])
# subprocess.call()	执行指定的命令，返回命令执行状态
print(type(result2))
print(result2)

print("#############shell=True##############")
print(subprocess.check_call('ls -l',shell=True))




print("***********************subprocess.check_output()***************************")


print("***********************subprocess.getoutput()***************************")
print("***********************subprocess.getstatusoutput()***************************")
# subprocess.getoutput(cmd)	接收字符串格式的命令，执行命令并返回执行结果，其功能类似于os.popen(cmd).read()和commands.getoutput(cmd)。
# subprocess.getstatusoutput(cmd)	执行cmd命令，返回一个元组(命令执行状态, 命令执行结果输出)，其功能类似于commands.getstatusoutput()。

result3=subprocess.getoutput(['ls','-l'])
print(result3)

status,result4=subprocess.getstatusoutput(['ls','-l'])
print("Status code: ",status)
print(result4)

import os

print("@@@@@@@@@@@@reading results line by line@@@@@@@@@@@@@@")

# results are in String format  
print(type(result4))
a=0
for i in result4.split('\n'):
    print("Line " + str(a) +": ",i)
    a=a+1

b=len(result4.split('\n'))
print("How many lines: ",b)