string=input().split(" ")
length=len(string) 
big_word=len(string[0])
word=string[0] 
for i in range(length):  
    each_word=len(string[i])
    if(each_word>big_word): 
        big_word=len(string[i]) 
        word=string[i]       
print(word)  

 
          
