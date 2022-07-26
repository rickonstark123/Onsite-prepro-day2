"""Math Symbol"""

def main():
    """Math Symbol"""
    result = 0
    process_ = []
    while True:
        input_ = input()
        if input_ == "+":
            result += int(input_)
            print("%.2f" %result)
            break
        elif input_ == "-":
            result -= int(input_)
            print("%.2f" %result)
            break
        elif input_ == "*":
            result *= input_
            print("%.2f" %result)
            break
        elif input_ == "/":
            result /= input_
            print("%.2f" %result)
            break
        process_.append(input_)
main()

        

