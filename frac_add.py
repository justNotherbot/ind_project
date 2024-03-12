def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())
c = int(input())
d = int(input())

lcm = (b * d) // gcd(b, d)
k_a = lcm // b
k_c = lcm // d

numerator = a * k_a + c * k_c
n_gcd = gcd(numerator, lcm)

print(numerator // n_gcd)
print(lcm // n_gcd)
