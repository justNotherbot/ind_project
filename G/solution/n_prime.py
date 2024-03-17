arr = [i for i in range(1, 1001)]
for i in range(1, len(arr)//2):
    if arr[i]:
        for j in range(i + arr[i], len(arr), arr[i]):
            arr[j] = 0

primes = []
for i in arr:
    if i and i != 1:
        primes.append(i)

n = int(input())
print(primes[n-1])
