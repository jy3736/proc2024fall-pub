def is_palindrome(number):
    return "YES" if str(number) == str(number)[::-1] else "NO"

if __name__ == "__main__":
    number = int(input("Enter a four-digit integer: "))
    print(is_palindrome(number))
