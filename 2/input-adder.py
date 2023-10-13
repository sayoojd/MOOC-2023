ans=0
while True:
    number=input("Please Enter each number to be added. Enter 'q' to get the answer\t")
    if number=='q':
        print("Thank You for using the program")
        break
    elif number.isdigit()== True:
        ans=ans+int(number)
    else:
        print("Please Enter a valid input")
print(f'\nThe sum of entered numbers is {ans}\n')