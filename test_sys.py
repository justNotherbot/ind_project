import subprocess
from os import walk
from os import path
import time

task = "A"
solution_nm = "solution.py"
#task = input("Which task do you want to solve? ")
#solution_nm = input("Provide the path to your solution: ")

test_path = task + "/tests"

filenames = next(walk(test_path), (None, None, []))[2]

n_correct = 0
n_total = len(filenames) // 2
t_avg = 0
t_min = 10 ** 10
t_max = -1

i_file = 1
for i in range(0, len(filenames), 2):
    in_file_path = path.join(test_path, str(i_file) + ".txt")
    out_file_path = path.join(test_path, str(i_file) + ".ans")

    t_in = open(in_file_path, "r")
    t_out = open(out_file_path, "r")
    t_in_cont = t_in.read().strip()
    t_out_cont = t_out.readlines()
    proc = subprocess.Popen(['python3', solution_nm, ''], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    t1 = time.time()
    proc.communicate(t_in_cont.encode("utf-8"))
    out = proc.communicate()[0].decode("utf-8")[:-1]  # Omit 2 special symbols at the end of the output
    t2 = time.time()
    out_lines = out.split("\n")
    out_lines = [s[:-1] for s in out_lines]
    t_out_cont = [s[:-1] for s in t_out_cont]

    dur = t2 - t1

    if dur < t_min:
        t_min = dur

    if dur > t_max:
        t_max = dur

    t_avg += dur


    if len(out_lines) == len(t_out_cont):
        right = True
        n_right = 0
        for j in range(len(out_lines)):
            ok = False
            for k in range(len(t_out_cont)):
                if sorted(out_lines[j]) == sorted(t_out_cont[k]):
                    ok = True
                    break
            right = ok
        if right:
            n_correct += 1
        #else:
        #    print(t_out_cont, out_lines)
            
    i_file += 1


t_avg /= n_total

print("Average time: {0}, Min time: {1}, Max time: {2}".format(t_avg, t_min, t_max))
if n_correct == n_total:
    print("Success!")
else:
    print("Your solution passed ", n_correct, " out of ", n_total, " tests.", "This is ", n_correct*100/n_total, "% of all tests.")
