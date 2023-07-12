# While loop that prints the numbers until the count of number reaches 0
number = 10
while number > 0 :
    number = number -1
    print(number)

# While loop that prints only the numbers from 50 to 0 that gets divided by 5
num2 = 50
while num2 > 0 :
    num2 = num2 -1
    if num2%5 == 0 :
        print(num2)
    else:
        continue


