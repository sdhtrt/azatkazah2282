def f(n, k):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return f(n-1, k) + k * f(n-2, k)


print(f(*[int(i) for i in input().split()]))
