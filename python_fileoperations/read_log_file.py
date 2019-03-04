# read audit.log file
# Only read the first 5 lines of a file
# The method readlines() reads until EOF using readline() and returns a list containing the lines.
# The method readline()reads one entire line from the file.
# The method readline()reads one entire line from the file. A trailing newline character is kept in the string.
# If the size argument is present and non-negative, it is a maximum byte count including the trailing newline and an incomplete line may be returned.


f = open("/home/nathan/dnf.log")
print("Type: " + str(type(f)))

lines=f.readlines()
print("Type: " + str(type(lines)))

print("Only read the first 5 lines")
i=0
for line in open("/home/nathan/dnf.log").readlines()[0:5]:
    print("Line " + str(i) + ': ' + line.strip())
    i=i+1

print("***************Only read the second line***********")
print(open("/home/nathan/dnf.log").readlines()[1])


print("***************Only read the the first five bytes***********")
i=0
for i in range(10):
    print(open("/home/nathan/dnf.log").readline(5))