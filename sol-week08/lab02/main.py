def can_split_chocolate(n, m, k):
    return "YES" if (k < n * m) and ((k % n == 0) or (k % m == 0)) else "NO"

if __name__ == "__main__":
    n, m, k = map(int, input("Enter n, m, k: ").split())
    print(can_split_chocolate(n, m, k))
