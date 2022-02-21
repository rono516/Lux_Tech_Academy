#This is a program to check whether a number
# entered is part of the fibonacci series
# Fibonacci series containes a set of numbers whose addition of 
# consequent numbers give the next number in series

number = int(input("Enter your number"))
zero = 0
firstOne = 1
secondOne =1

if number == 0 or number == 1:
    print(f'{number} is part of the fibonacci series')
    
else:
    while zero< number:
        zero = firstOne+ secondOne
        secondOne = firstOne
        firstOne= zero
        
        if zero == number:
            print(f'{number} is in series')
        else:
            print(f'{number} is not part of series')    


    