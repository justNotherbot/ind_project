arr = [i for i in range(1, 1001)]
for i in range(1, len(arr)//2):
    if arr[i]:
        for j in range(i + arr[i], len(arr), arr[i]):
            arr[j] = 0

primes = {}
idx = 1
for i in arr:
    if i and i != 1:
        primes[i] = idx
        idx += 1

n = int(input())

if n in primes:
    print(primes[n])
else:
    print(-1)
