#a sample of a function
def add_eight_or_three(input_num):
    if input_num>=10:
        result=input_num+8
        
    else:
        result=input_num+3  
    return result
galv=add_eight_or_three(9)
print(galv)