def get_ans(primes, n, prev, prefix):
    if n < 0:
        return
    elif n == 0:
        print(prefix[1:])
        exit()
    
    for i in primes:
        if prev < i <= n:
            get_ans(primes, n-i, i, prefix + "+" + str(i))


arr = [i for i in range(1, 1001)]
for i in range(1, len(arr)//2):
    if arr[i]:
        for j in range(i + arr[i], len(arr), arr[i]):
            arr[j] = 0

primes = []
for i in arr:
    if i and i != 1:
        primes.append(i)

get_ans(primes, int(input()), 0, "")
