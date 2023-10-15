while True:
    num= input("Enter the number to be squared! Enter 'q' to Quit")
    if num=='q' or num=='Q':
        break
    elif num.isdigit()==True:
        print(f"The square of {num} is {int(num) * int(num)}")
    else:
        print("Please enter a valid input")
    