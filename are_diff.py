def gcd(a, b):
    while b:
        a, b = b, a % b
    
    return a


a, b = map(int, input().split())
if gcd(a, b) == 1:
    print("YES")
else:
    print("NO")
