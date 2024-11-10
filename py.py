import json

dict1 = {}
employee_list = {}
n = int(input("ENTER THE NUMBER OF EMPLOYEES: "))

# Getting employee data
for x in range(n):
    name = input("ENTER NAME: ")
    salary = int(input("ENTER SALARY: "))
    dict1[name] = salary

# Sorting the employees manually by salary in descending order
sorted_employees = []
while dict1:
    # Find the employee with the highest salary
    highest_salary_employee = max(dict1, key=dict1.get)
    highest_salary = dict1.pop(highest_salary_employee)
    sorted_employees.append((highest_salary_employee, highest_salary))

# Adding sorted employees to employee_list
for name, salary in sorted_employees:
    employee_list[name] = salary

# Printing the sorted employee list in a nicely formatted JSON
print(json.dumps(employee_list, indent=5))
