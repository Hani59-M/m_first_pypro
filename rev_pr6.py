def reverse_count(n):
    if n == 0:
        return
    print(n)
    reverse_count(n - 1)

reverse_count(1000)
