# read audit.log file
# Only read the first 5 lines of a file


f = open("/home/nathan/dnf.log")
print("Type: " + str(type(f)))

lines=f.readlines()
print("Type: " + str(type(lines)))

print("Only read the first 5 lines")
i=0
for line in open("/home/nathan/dnf.log").readlines()[0:5]:
    print("Line " + str(i) + ': ' + line.strip())
    i=i+1

