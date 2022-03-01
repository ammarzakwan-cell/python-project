# Python program to find all string; credit to geeksforgeeks
# which are equal given length k 
  
# function find sttring equal length k 
def string_k(k, str): 
      
    # create the empty string 
    string = [] 
      
    # split the string where space is comes 
    text = str.split() 
      
    # iterate the loop till every substring 
    for x in text: 
          
        # if length of current sub string 
        # is equal k then 
        if len(x) == k: 
              
            # append this sub string in 
            # string list 
            string.append(x) 
              
     # return string list 
    return string 
  
# Driver Program      
k = 8

# Open a file: file
file = open('myfile.txt', "r")
 
# read all lines at once
str = file.read()
 
# close the file
file.close()

print(*string_k(k, str), sep="\n")
