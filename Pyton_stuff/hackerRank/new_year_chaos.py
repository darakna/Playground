import time
#t1 = 0
#t2 = 0
# Complete the minimumBribes function below.
# Print an integer denoting the minimum number of bribes needed to get the queue into its final state.
# Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than 2 people.
# Any person in the queue can bribe the person directly in front of them to swap positions.

def check_if_sorted(q):
    #global t2
    #t2 = t2 - time.perf_counter_ns()
    for elem in range(len(q[:-1])):
        if q[elem] > q[elem + 1]:
            #t2 = t2 + time.perf_counter_ns()
            return False
    #t2 = t2 + time.perf_counter_ns()
    return True

def check_if_sorted2(q):
    if all(q[i] <= q[i + 1] for i in range(len(q) - 1)):
        return True
    return False


def minimumBribes(q):
    too_chaotic = "Too chaotic"
    total_bribes = 0
    while not check_if_sorted2(q):
        bribe_overflow = 0
        elem = 0
        while elem < (len(q) - 1):
            if q[elem] > q[elem + 1]:
                tmp = q[elem]
                q[elem] = q[elem + 1]
                q[elem + 1] = tmp
                bribe_overflow += 1
                if bribe_overflow > 2:
                    return too_chaotic
                total_bribes += 1
                elem += 1
            else:
                bribe_overflow = 0
                elem += 1
                continue
    return total_bribes

print("3 =", minimumBribes([2, 1, 5, 3, 4]))
print("Too chaotic =", minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]))
print("7 =", minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))
print("0 =", minimumBribes([1, 2, 3, 4, 5, 6, 7, 8]))
print("Too chaotic =", minimumBribes([2, 5, 1, 3, 4]))
print("Too chaotic =", minimumBribes([2, 5, 1, 3, 4]))
print("Nullcase 0 =", minimumBribes([]))
print("One item in list  0 =", minimumBribes([1]))

f = open("input07_bribe_fail.txt", "r")
lines = f.read().split("\n")
t = int(lines[0])
results_input07_bribe_fail = [115173, "Too chaotic", 115013, "Too chaotic"]
for t_itr in range(t):
    n = int(lines[1 + t_itr * 2])
    q = list(map(int, lines[2 + t_itr * 2].rstrip().split()))
    print(results_input07_bribe_fail[t_itr], "=", minimumBribes(q), "n =", n, "len(q) =",len(q))
