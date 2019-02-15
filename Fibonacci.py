# Filename Fibonacci.py
# July 11, 2018 by Xinhao


print('This program demonstrates the Fibonacci sequence.')

loop = True

while loop == True:

    number = int(input('Please enter an integer larger than 1: '))

    i = 0
    Fibonacci =[1,1]

    if number > 50:
        print('Are you crazy?!')

    while i < (number-2):
        Fibonacci.append(Fibonacci[i]+Fibonacci[i+1])
        i = i+1

    print(Fibonacci)
    s = (input('Do you want to continue? (Y/N) '))
    if s == "N" or s == 'n':
        loop = False

print('Good choice')
print('Calculation completed')
