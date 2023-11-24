import math

def calculate_square_root():
    try:
        num = float(input("Enter a number: "))
        if num >= 0:
            print(f"The square root of {num} is {math.sqrt(num)}")
        else:
            print("Error: Please enter a non-negative number.")
    except ValueError:
        print("Error: Please enter a valid number.")

calculate_square_root()
