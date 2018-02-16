#MIT 6_0001 Problem set 01 Part B 
#For assignment details visit:
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/
#


#Starting annual salary
annual_salary = float(input('Please enter the starting annual salary:'))

#Initialize semi-annual raise
semi_annual_raise = float(input('Please enter (as a decimal percentage) a semi-annual raise:'))

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


def calculate_down_payment(cost, portion_payment):
    return cost*portion_payment

def calculate_monthly_savings(salary, portion_saved):
    return (salary/12)*portion_saved

down_payment = calculate_down_payment(total_cost, portion_down_payment)

monthly_savings = calculate_monthly_savings(annual_salary, portion_saved)

months = 0
while current_savings<=down_payment:
    if (months-1)%6==0 and (months-1)!=0:
        annual_salary += semi_annual_raise*annual_salary
        monthly_savings = calculate_monthly_savings(annual_salary, portion_saved)
    current_savings += monthly_savings + current_savings*r/12
    months += 1
    
    
print(months, current_savings)
