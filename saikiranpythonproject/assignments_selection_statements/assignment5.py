def find_max(num1,num2):
    max_num=-1
    temp=num1
    while(temp<=num2):
        if (temp%3==0 and temp%5==0):
            max_num=temp
            break
        temp+=1
    return max_num

max_num=find_max(10,15)
print(max_num)