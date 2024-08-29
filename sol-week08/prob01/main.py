def digits_in_ascending_order(number):
    digits = [int(d) for d in str(number)]
    return "YES" if digits == sorted(digits) else "NO"

if __name__ == "__main__":
    number = int(input("Enter a three-digit integer: "))
    print(digits_in_ascending_order(number))

