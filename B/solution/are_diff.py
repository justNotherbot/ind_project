def gcd(a, b):
    while b:
        a, b = b, a % b
    
    return a


a = int(input())
b = int(input())

if gcd(a, b) == 1:
    print("YES")
else:
    print("NO")
