import re

# Open a file: file
file = open('myfile.txt', "r")
 
# read all lines at once
str = file.read()
 
# close the file
file.close()

emailRegex = re.compile(r'''(
([a-zA-Z0–9_\-\.]) +
@gmail.com
)''', re.VERBOSE)

mo = emailRegex.findall(str)
print(*mo, sep="\n")