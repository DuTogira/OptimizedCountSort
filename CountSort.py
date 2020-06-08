# Combined complexity of improved count sort algorithm:
# For the purpose of analysis, k is the number of unique values in our input,
# R is the number of non-numeric values in our input,
# S is the number of numeric values in our input,
# r is the number of unique Non-numeric values in our input,
# and s is the number of unique numeric values in our input.
# By definition, r + s = k, and R + S = n
# Runtime Complexity: O(n + k*log(k))
# O(n) best for sufficiently small k, O(n + k*log(k)) average,
# O(n*log(n)) worst when every value in our input is unique.
# Space Complexity: O(n) best/average/worst. Technically O(k + n) but k <= n always, reduces to O(n)

# Since this algorithm is composed of count sort combined with TimSort, it is stable,
# meaning that same-value input maintains its order as output.

import cProfile
from random import shuffle


# Based on performance tests, duSort runs ~2 times slower than TimSort, even though its asymptotic run-time is better
# This is because it practically takes as long to build the count dictionaries as it takes for TimSort to sort the data
# This analysis makes the assumption that both algorithms must split data into numeric v non-numeric sub-sets
# Currently duSort becomes competitive with TimSort when < 5% of input data is unique.
def duSort(a: list) -> list:
    # aux = []
    # aux_alph = []
    count_nums = dict()
    # count_nums_aux = dict()
    # Runtime for splitting input array: O(n)
    # Space complexity: 0(n)
    # for i in range(0, len(a)):
    #    try:
    #        aux.append(float(a[i]))
    #    except ValueError:
    #        aux_alph.append(a[i])
    # Runtime building count_nums: O(S)
    # Space Complexity: O(S) where S is the number of
    # numeric elements within our input a
    # By definition, S <= n
    for i in range(0, len(a)):
        if a[i] in count_nums:
            count_nums[a[i]] += 1
        else:
            count_nums[a[i]] = 1
    # Runtime building count_nums: O(R)
    # Space Complexity: O(R) where R is the number of
    # non numeric elements within our input a
    # By definition, R <= n
    # for i in range(0, len(aux_alph)):
    #    if aux_alph[i] in count_nums_aux:
    #        count_nums_aux[aux_alph[i]] += 1
    #    else:
    #        count_nums_aux[aux_alph[i]] = 1

    i = 0
    # Runtime adjusting count_nums to contain output positions: O(n-alpha) + O(r*log(r)),
    # where r is the number of distinct elements in R
    # Space Complexity: O(r)
    # for key in sorted(count_nums_aux.keys()):
    #    for j in range(0, count_nums_aux[key]):
    #        a[i + j] = key
    #    i += count_nums_aux[key]
    # Runtime adjusting count_nums to contain output positions: O(n-int) + O(s*log(s)),
    # where s is the number of distinct elements in S
    # Space Complexity: O(s)
    for key in sorted(count_nums.keys()):
        for j in range(0, count_nums[key]):
            a[i + j] = key
        i += count_nums[key]
    return a
    # Total runtime: O(n) + O(s*logs) + O(r*logr) --> O(n) + O(k*logk) --> O(n + k*logk)
    # Total space: O(n) + O(s) + O(r) --> O(n + k) where k <= n always --> O(n)


def benchmark(a: list):
    aux: list = []
    aux_alph: list = []
    for i in range(0, len(a)):
        try:
            aux.append(float(a[i]))
        except ValueError:
            aux_alph.append(a[i])
    a = sorted(aux)
    a.append(sorted(aux_alph))
    return a


def duSortTest(a: list):
    aux: list = []
    aux_alph: list = []
    for i in range(0, len(a)):
        try:
            aux.append(float(a[i]))
        except ValueError:
            aux_alph.append(a[i])
    a = duSort(aux)
    a.append(duSort(aux_alph))
    return a


# Basic main function for testing and debugging. Not critical to the algorithm
if __name__ == '__main__':
    with open('input6.txt', 'r') as f:
        data = f.read()
        data = data.split()
        shuffle(data)
    cProfile.run('benchmark(data)')
    cProfile.run('duSortTest(data)')
    #data = duSortTest(data)
    #print(data)
