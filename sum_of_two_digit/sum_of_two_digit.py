def get_sum(a, b):
    a = int(a)
    b = int(b)
    return a + b

if __name__ == "__main__":
    a, b = input().split()
    print(get_sum(a, b))