n=input()
min_element=(min(n))  
remaining=""
for i in n:
    if(i==min_element):
        pass
    else:
        remaining+=i 
reversed=remaining[::-1]  
print(min_element+remaining+reversed+min_element) 

        

