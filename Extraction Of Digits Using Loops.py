

def extract_digits_from_number(num):
    value = num
    while value > 0:
        digit = value % 10
        value = value // 10
        print(digit, end='')
    print()

# take user input
user_number = int(input("Enter a number: "))

extract_digits_from_number(user_number)


    
    
    

    