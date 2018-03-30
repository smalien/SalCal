import re

def calculateQuebecTax(salary):
  if salary <= 42705:
    quebecTax = salary * .16
    return quebecTax
  elif salary > 42705 and salary <= 85405:
    newBracket = (salary-42705)
    quebecTax = (42705 * .16) + (newBracket * .20)
    return quebecTax
  elif salary > 85405 and salary <= 103915:
    newBracket = (salary-85405)
    quebecTax = (42705 * .16) + (42700 * .20) + (newBracket * .24)
    return quebecTax
  elif salary > 103915:
    newBracket = (salary-103915)
    quebecTax = (42705 * .16) + (42700 * .20) + (18510 * .24) + (newBracket * .2575)
    return quebecTax

def calculateCanadaTax(salary):
  if salary <= 45916:
    canadaTax = salary * .15
    return canadaTax
  elif salary > 45916 and salary <= 91831:
    newBracket = (salary-45916)
    canadaTax = (45916 * .16) + (newBracket * .205)
    return canadaTax
  elif salary > 91831 and salary <= 142353:
    newBracket = (salary-91831)
    canadaTax = (45916 * .16) + (45915 * .205) + (newBracket * .26)
    return canadaTax
  elif salary > 142353 and salary <= 202800:
    newBracket = (salary-142353)
    canadaTax = (45916 * .16) + (45915 * .205) + (50522 * .26) + (newBracket * .29)
    return canadaTax
  elif salary > 202800:
    newBracket = (salary-202800)
    canadaTax = (45916 * .16) + (45915 * .205) + (50522 * .26) + (60447 * .29) + (newBracket * .33)
    return canadaTax 

print "-------------------------------------------------------------------------------"
print "Select 's' and enter your salary to find out your wage, or select 'w' and enter your wage to find out your salary\n"
salaryOrWage = raw_input("Please select one of the following [s/w]: ").lower()
print
while salaryOrWage != "s" and salaryOrWage != "w":
  salaryOrWage = raw_input("Please select one of the following [s/w]: ").lower()
if salaryOrWage == "s":
  salary = raw_input("Please enter your annual salary: ")
  print
  salary = float(re.sub("[^0-9\.]", "", salary))
  formattedSalary = '${:,.2f}'.format(salary)
  print "Annual salary: "+formattedSalary
  hourlyWage = round(float(salary)/float(2080), 2)
  formattedHourlyWage = '${:,.2f}'.format(hourlyWage)
  print "Hourly wage: "+formattedHourlyWage+"/h"
elif salaryOrWage == "w":
  hourlyWage = raw_input("Please enter your hourly wage: ")
  print
  hourlyWage = float(re.sub("[^0-9\.]", "", hourlyWage))
  formattedHourlyWage = '${:,.2f}'.format(hourlyWage)
  print "Hourly Wage: "+formattedHourlyWage+"/h" 
  salary = hourlyWage*2080
  formattedSalary = '${:,.2f}'.format(salary)
  print "Annual Salary: "+formattedSalary
provincialTax = calculateQuebecTax(salary)
formattedProvincialTax = '${:,.2f}'.format(provincialTax)
print "Provincial income tax: "+formattedProvincialTax
federalTax = calculateCanadaTax(salary)
formattedFederalTax = '${:,.2f}'.format(federalTax)
print "Federal income tax: "+formattedFederalTax
taxes = provincialTax + federalTax
takehome = (salary - taxes)
formattedTakehome = '${:,.2f}'.format(takehome)
print "Take-home: "+formattedTakehome