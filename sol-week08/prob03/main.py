def find_outlier_index(a, b, c):
    if a == b:
        return 3
    elif a == c:
        return 2
    else:
        return 1

if __name__ == "__main__":
    a, b, c = map(int, input("Enter three integers: ").split())
    print(find_outlier_index(a, b, c))

    