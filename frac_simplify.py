def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())
n_gcd = gcd(a, b)

print(a // n_gcd)
print(b // n_gcd)
