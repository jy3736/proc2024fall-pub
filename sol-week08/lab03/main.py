def find_minimum(a, b, c):
    return min(a, b, c)

if __name__ == "__main__":
    a, b, c = map(int, input("Enter three integers: ").split())
    print(find_minimum(a, b, c))
    