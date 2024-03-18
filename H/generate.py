import subprocess
import os
import random


N_TESTS_TO_GEN = 100
SAVE_ANS = True

arr = [i for i in range(1, 1001)]
for i in range(1, len(arr)//2):
    if arr[i]:
        for j in range(i + arr[i], len(arr), arr[i]):
            arr[j] = 0

primes = []
for i in arr:
    if i and i != 1:
        primes.append(i)

def get_new():
    n_add = random.randint(1, 20)
    step = len(primes) // n_add
    lwr = step
    prev = random.randint(1, step)
    total = primes[prev]
    for i in range(n_add-1):
        prev = random.randint(prev+1, step+prev)
        total += primes[prev]

    token = str(total)
    in_str = str(total)+"\n"
    return token, in_str


curr_dir = os.path.dirname(os.path.realpath(__file__))
sln_path = os.path.join(curr_dir, "solution")
tests_path = os.path.join(curr_dir, "tests")
filenames = next(os.walk(sln_path), (None, None, []))[2]
print(filenames)

if not len(filenames):
    print("Solution not found")
    exit(0)

sln_full_path = os.path.join(sln_path, filenames[0])

tokens = {}

for i in range(1, N_TESTS_TO_GEN+1):
    token, in_str = get_new()
    while token in tokens:
        token, in_str = get_new()
    tokens[token] = 1
    
    f = open(os.path.join(tests_path, str(i)+".txt"), "w")
    f.write(in_str)
    f.close()

    if SAVE_ANS:
        in_bytes = in_str.encode('utf-8')
        f = open(os.path.join(tests_path, str(i)+".ans"), "w")
        proc = subprocess.Popen(['python3', sln_full_path, ''], stdin=subprocess.PIPE,\
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        proc.communicate(in_bytes)
        out = proc.communicate()[0].decode("utf-8")[:-1]
        assert(len(out) > 0)
        
        f.write(out)

        f.close()
