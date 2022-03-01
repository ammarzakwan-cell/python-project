import os
os.chdir('C:/Users/username/Downloads')

def analysis(s):  
    text = s.split()
    file = open("results.txt","w")
    
    #Create a dictionary that defines each unique word in the file and stores its frequency
    wordfreq = []
    for x in text:
        #Sort the dictionary in descending order
        text.sort(reverse = True)
        wordfreq.append(text.count(x))
    file.write(f'Frequencies each word\n' + str(list(zip(text, wordfreq))))
    
    #Count how many times the word “it” occurs in the file
    count = text.count('it')
    
    file.write(f'\n{count}\n')

    #Find words that end with ‘ly’ in the file 
    for text in s.split():
        if text.endswith("ly"):
            file.write(f'{text}\n') 
 
    file.close()
    
with open('recipe_ital_115.txt') as f:

    s = f.read()
    #call function
    analysis(s)














