year=int(input("enter current year"))
year1=int(input("enter final year"))
print("list of leap years are")
for leap in range(year,year1):
    if(leap%4==0)and(leap%100!=0)or(leap%400==0):print(leap)
