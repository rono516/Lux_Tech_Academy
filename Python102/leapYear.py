
#This is a python program to check if a year is a leap year
#a leap year is divisible by 4 and by 400 if it ends with two zeros e.g 2000



year = int(input("Enter year to check: "))
LeapYear = year%4
LeapCentury = year%100
Leap2Century = year%400


if LeapYear == 0 and LeapCentury != 0:
      
  print(f"{year} is a Leap Year")

elif LeapCentury == 0 and Leap2Century == 0:

  print(f"{year} is a Leap Centuary Year" )

else:

  print(f"{year} is not a Leap Year")