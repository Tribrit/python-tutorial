def evaluate_temp(temp):
    message="Normal temperature."
 #Adding a condition to check temperture
 #Nb:for a block of code in a function are supposed to be indented

    if temp > 38:
       message="Fever!"
    return message
print(evaluate_temp(37))