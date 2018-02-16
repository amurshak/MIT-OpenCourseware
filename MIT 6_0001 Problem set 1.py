#MIT 6_0001 Problem set 01 
#For assignment details visit:
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/
#


#Starting annual salary
annual_salary = float(input('Please enter the starting annual salary:'))

#Portion of salary saved each month for down payment
portion_saved = float(input('Please enter the portion of salary to be saved:'))

#Total cost of dream home
total_cost = float(input('Please enter the cost of your dream home:'))

#Portion of cost needed for a down payment
portion_down_payment = 0.25

#Current savings initialized
current_savings = 0

#Annual return rate of savings
r = 0.04

annual_return = current_savings*r/12

def calculate_down_payment(cost, portion_payment):
    return cost*portion_payment


down_payment = calculate_down_payment(total_cost, portion_down_payment)

monthly_savings = (annual_salary * portion_saved)/12

months = 0
while current_savings<down_payment:
    months += 1
    current_savings += monthly_savings
    current_savings += current_savings*r/12
    
    
print(months, current_savings)
