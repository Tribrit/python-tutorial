#This is to help a friend calculate his pay after tax has been taken away from his salary
def get_pay(num_hrs,hourly_wage ,tax_bracket):
    #pre-tax pay ,based on receiving $/hour
    pre_tax=num_hrs*hourly_wage
    #pay after tax,based on a tax bracket
    pay_aftertax=pre_tax*(1-tax_bracket)

    return pay_aftertax
pay_fulltime=get_pay(40,15,0.12)
print(pay_fulltime)