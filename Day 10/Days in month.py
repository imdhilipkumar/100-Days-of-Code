# days in month 
# to find the leap year 
def is_leap(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

# to find the days in month 
def Days_in_month(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month==2:
        return 29
    return month_days[month-1]

year=int(input("Enter the Year :"))
month=int(input("Enter the Month :"))
days=Days_in_month(year,month)
print(days)

    