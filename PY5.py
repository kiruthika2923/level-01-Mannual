print("Kiruthika International [P] Ltd")
print("No.15, Naggapura Dist, Bengaluru")
print("-------------------------------")
print("Employee Payroll System")
print("-------------------------------")
id=int(input("Enter the Employee id:"))
name=input("Enter the employee Name:")
salary=int(input("Enter the Salary:"))
print("INCOME")
bonus=salary*20/100
print("Bonus 20% is:",bonus)
ot=salary*10/ 100
print("Overtime 10% is:", ot)
ta=salary*5/100
print("Travel Allowance 5% is:",ta)
gpay=bonus+ot+ta+salary
print("Gross Pay in Rupees:",gpay)
