#year = int(input("Enter year: "))

def isLeap(year):
    if year%4 == 0 and year%100 == 0:
        return (f' {year} is a leap year')
    else   :
        return(f'{year} is not a leap year')

print(isLeap(2015))
