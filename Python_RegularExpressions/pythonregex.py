#Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
#re 模块使 Python 语言拥有全部的正则表达式功能。
#compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。

#re.match函数, re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# re.match(pattern, string, flags=0)

import re
print(re.match("www","www.baidu.com").span())
print(re.match("www.","www.baidu.com").span())
print(re.match("wwww","www.baidu.com"))
print(re.match("baidu","www.baidu.com"))
print(re.match("www","www.baidu.com"))

m=re.match("wwww","www.baidu.com")

if m==None:
    print("www is not included in www.baidu.com")
else:
    print("www is included in www.baidu.com")

print("----------------------------")

line="Cats are smarter than dogs"
matchobj_01 = re.match(".*",line)
print(matchobj_01.group())

matchobj_02=re.match("Cats|dogs",line)
print(matchobj_02.group())

matchobj_03=re.match("(Cats|dogs)\sare\s(smarter|lazier)\sthan\s",line)
print(matchobj_03.group())

matchobj_04=re.match("(Cats|dogs)\sare\s(smarter|lazier)\sthan\s",line)
print("matchobj_04.group(0):", matchobj_04.group(0))
print("matchobj_04.group(1):", matchobj_04.group(1))
print("matchobj_04.group(2):", matchobj_04.group(2))



#re.search 扫描整个字符串并返回第一个成功的匹配。
print("re.search testing")
print(re.search("www","www.baidu.com"))
print(re.search("www","www.baidu.com").span())
print(re.search("com","www.baidu.com"))
print(re.search("baidu","www.baidu.com").span())

line2="cats are smarter than dogs and cats"
print(re.search("cats",line2))
print(re.search("cats",line2).span())
print("searching 'cat':", re.search("cat",line2).span())

#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

line = "Cats are smarter than dogs";

matchObj_05 = re.match(r'dogs', line, re.M | re.I)

if matchObj_05:
    print("match --> matchObj.group() : ", matchObj_05.group())
else:
    print("Not match")

if matchObj_05!="True":
    print("false")

a=5==5
print(a)
if a==True:
    print("Great")

if a=="True":
    print("Great!!!")
else:
    print("WRong!!!!")



#检索和替换
#Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
#substitute
#re.sub(pattern, repl, string, count=0, flags=0)

phone="2004-959-559 # 这是一个国外电话号码"
#delete the python comment
number=re.sub(r'#.*$',"",phone)
print("The telephone number is: ", number)

number2=re.sub("\d{4}","",phone)
print(number2)

number3=re.sub("\d{4}\-\d{3}\-\d{3}","",phone)
print(number3)

number4=re.sub("\-","",phone)
print(number4)



#re.match()
#re.search()
#re.sub()
#re.compile()

#compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
pattern=re.compile("\d+")
m=pattern.match("one12twothree34four")
#no match, return None
print(m)

m = pattern.match('one12twothree34four', 3, 10)
print(m)


print(m.group())
print(m.start())
print(m.end())
print(m.span())

#m.group(), return matched content
#m.start(), m.end(), m.span()
#group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
#start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
#end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
#span([group]) 方法返回 (start(group), end(group))。

#pattern.findall()
#在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。



#re.split()
#split 方法按照能够匹配的子串将字符串分割后返回列表.
#re.split(pattern, string[, maxsplit=0, flags=0])

print(re.split("\W+","nathan,zhang,wang"))

print(re.split('\d+',"nathan,zhang,123"))



#use python to analyze logs
#groupdict()
#它返回一个字典，包含所有经命名的匹配子群，键值是子群名。
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print(m.groupdict())
# {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}


#https://www.cnblogs.com/i-honey/p/7783664.html

# python 中单引号、双引号和三引号的区别
logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''
pattern = '''(?P<remote_addr>[\d\.]{7,}) - - (?:\[(?P<datetime>[^\[\]]+)\]) "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "(?:[^"]+)" "(?P<user_agent>[^"]+)"'''

print(re.match(pattern,logline).groupdict())

