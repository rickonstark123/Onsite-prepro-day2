"""measure"""

def main():
    """measure"""
    num_fix = int(input())
    num0 = 0
    if num_fix == 0:
        print("No Tape Measure")
    while num_fix != 0:
        num1 = input()
        if num1 == "No more!":
            if num0 != 0:
                print("Sum of Found Number =", str(num0))
            else:
                print("Not Found Number")
            break
        elif int(num1) <= num_fix:
            num0 = int(num1) + num0
main()
#1234
           
