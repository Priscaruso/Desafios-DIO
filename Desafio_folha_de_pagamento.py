#enter the employee number
emp_no = int(input())

#enter the number of hours the employee worked
worked_hours = int(input())

#enter how much the employee receives per worked hour
receives_per_worked_hour = float(input())

#calculates the employee salary
salary = (worked_hours)*(receives_per_worked_hour)

#displays the employee number and its salary with two decimal places
print("NUMBER = {}".format(emp_no),end="\n")
print("SALARY = U$ %0.2f"%salary,end="\n")