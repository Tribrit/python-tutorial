def evaluate_temp(temp):
    if temp> 38:
       message="Fever!"
    elif temp > 35:
        message="normal temperature"
    else :
        message="low temperature!"
    return message
print(evaluate_temp(34))   
