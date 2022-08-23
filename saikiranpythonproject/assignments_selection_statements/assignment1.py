def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if (num3>=num1+num2):
        return failure
    elif (num1>=num3+num2):
            return failure
    elif (num2>=num1+num3):
        return failure
    else :
        return success
    

print(form_triangle(3,4,5))
print(form_triangle(3,9,3))