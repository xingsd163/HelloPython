print("the length of this statement is: " + str(len("this is a test")))

a="this is a file you should be familiar with"

if "this is an" in a:
    print("'this is an'" + "is in the object a")
elif "this a ann" in a:
    print("'this is ann'" + "is in the object a")
else:
    print("Wrong")

print(a.endswith("with"))
print(a.endswith("en"))

b="100"
if b==100:
    print("b=100")
else:
    print("b!=100")

if int(100) == 100:
    print("Correct")
else:
    print("Wrong")

#type conversion, single-line comment
'''
sdfsdfsdfsdfsfsdf, multiline comment
'''

#split words into several parts

str="this is my first first-kiss"
print(str.split(' ',3))
print(str.split(' ',2))
print(str.split())

writeline="ads\n"

try:
    readlogfile=open("/home/nathan/secure.txt","r")
    print(readlogfile.readlines())
except IOError:
    print("File not found")
else:
    readlogfile.close()

try:
    writelogfile=open("/home/nathan/secure.txt","a+")
    writelogfile.write(writeline)

except IOError:
    print("File not exist")
else:
    writelogfile.close()



str02="type=USER_START msg=audit(1547111799.648:576): pid=7511 uid=1001 auid=1001 ses=3 subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023"
splitted_list=str02.split(' ',6)

print(type(splitted_list))


print(splitted_list)

for each in splitted_list:
    item=each.split("=")
    print(item)
    print("---------------------")
    for sub_item in item:
        print(sub_item)



a="I am Chinese" is "I am Chinese"
b="I am Chinese" is not "I am CHinese"

#print can print multiple objects at one time

print(a,b)
print(a,b,a,b,b,a,a)


#strip,lstrip,rstrip

a=" sdfsfs "
print(a.lstrip(),len(a))
print(a.rstrip(),len(a))


#replace

a="this is my second first-kiss"
b=a.replace("first","First")
print(b)

c=a.replace("-","--")
print(c)

a="a,b,c,d,e,f,s,d"
b=a.replace(",","|")
print(b)

#rfind(), return the positions of the last seen

a="Hello World,Hello Python, Hello Java"
b="JAVA"
c="java"
if b in a:
    print("b in a")
elif c in a:
    print("c in a")
else:
    print("b and c not in a")


if a.rfind(b) >=0:
    print("b in a")
else:
    print("b not in a")


print("--------------------")

if a.rfind(b) ==-1:
    print("b not in a")
else:
    print("b in a")

print("--------------------")


# print format

print("Total number: %d" % 100)


a=(a,'b',123)
print("THE LENGHT OF THIS OBJECT: ",len(a),"\nTHE TYPE OF THIS OBJECT: ",type(a))










