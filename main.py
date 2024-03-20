# Lab 6 Version Control - Simple Encoder

def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def encode(passcode):
    """
    Simple encoder to add 3 to each digit of the passcode. If >9 after edition loops back to 0 for digit
    :param passcode:
    :return: encoded passcode
    """
    encoded = ""
    for digit in passcode:
        num = int(digit)
        num = num + 3
        if num >= 10:
            num = num - 10
        num_str = str(num)
        encoded += num_str

    return encoded


def decode(passcode):
    """
    Write your method description here
    :param passcode:
    :return: encoded_passcode
    """
    #Add decoder code here then push to repository with comment added decode function
    pass

def main():

    encoded = ""
    decoded = ""

    while True:
        print_menu()

        user_input = input("Please enter an option: ")

        if user_input == "3":
            break

        elif user_input == "1":
            passcode_input = input("Please enter your password to encode: ")
            encoded = encode(passcode_input)
            print("Your password has been encoded and stored!")
            print()

        elif user_input == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")

        else:
            print("Invalid input")

if __name__ == "__main__":
    main()