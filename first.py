n=input().split() 
integer_of_n=map(int,n) 
form_of_list=(list(integer_of_n)) 
count_min=min(form_of_list)
length_of=len(form_of_list) 
count=count_min 
for i in range(length_of):
    count+=1 
    if(count not in form_of_list):
        print(count)
        break 
    
