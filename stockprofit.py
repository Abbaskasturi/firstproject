n=input().split(",") 
numbers=list(map(int,n)) 
count=0 
max_list=[]
for i in numbers:
    sub_num=numbers[count:]  
    for j in sub_num: 
        if(j>i): 
            ma=j-i  
            max_list.append(ma)
    count+=1  
print(max(max_list)) 



    