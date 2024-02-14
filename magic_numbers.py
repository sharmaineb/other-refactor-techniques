# by Kami Bigdely 
# Replace magic numbers with named constanst

# First Section
# Given two point charges, calcualte the electric force exerted on them.
class Constants:
    ELECTRIC_CONSTANT = 8.9875517923e9

def calculate_electric_force(q1, q2, distance):
    force = Constants.ELECTRIC_CONSTANT * q1 * q2 / (distance ** 2)
    return force

def check_even_odd(num):
    return 'even' if num % 2 == 0 else 'odd'

def main():
    q1 = int(input('Enter a value of charge q1: '))
    q2 = int(input('Enter a value of charge q2: '))
    distance = int(input("Enter the distance between two charges: "))
    
    force = calculate_electric_force(q1, q2, distance)
    print("Electric Force between q1 and q2 is:", force, "Newton")

    num = int(input('Enter an integer number: '))
    print(num, "is an", check_even_odd(num), "number.")

if __name__ == "__main__":
    main()
