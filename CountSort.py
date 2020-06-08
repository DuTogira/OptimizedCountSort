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

base = 35


# Based on performance tests, duSort performs faster than TimSort when 50% or more of data is duplicated.
# When all input is unique, duSort runs ~ 2 times slower than TimSort.
# This analysis makes the assumption that both algorithms must split data into numeric v non-numeric sub-sets
def duSort(a: list):
    aux = []
    aux_alph = []
    count_nums = dict()
    count_nums_aux = dict()
    # Runtime for splitting input array: O(n)
    # Space complexity: 0(n)
    for num in a:
        if num.lstrip('-').isdigit() or num.replace('.', '').isdigit():
            aux.append(float(num))
        else:
            aux_alph.append(num)
    # Runtime building count_nums: O(S)
    # Space Complexity: O(S) where S is the number of
    # numeric elements within our input a
    # By definition, S <= n
    for num in aux:
        if num in count_nums:
            count_nums[num] += 1
        else:
            count_nums[num] = 1
    # Runtime building count_nums: O(R)
    # Space Complexity: O(R) where R is the number of
    # non numeric elements within our input a
    # By definition, R <= n
    for elem in aux_alph:
        if elem in count_nums_aux:
            count_nums_aux[elem] += 1
        else:
            count_nums_aux[elem] = 1
    # Runtime adjusting count_nums to contain output positions: O(n-int) + O(s*log(s)),
    # where s is the number of distinct elements in S
    # Space Complexity: O(s)
    i = 0
    for key in sorted(set(aux)):
        while count_nums[key]:
            a[i] = key
            i += 1
            count_nums[key] -= 1
    # Runtime adjusting count_nums to contain output positions: O(n-alpha) + O(r*log(r)),
    # where r is the number of distinct elements in R
    # Space Complexity: O(r)
    for key in sorted(set(aux_alph)):
        while count_nums_aux[key]:
            a[i] = key
            i += 1
            count_nums_aux[key] -= 1
    return a
    # Total runtime: O(n) + O(s*logs) + O(r*logr) --> O(n) + O(k*logk) --> O(n + k*logk)
    # Total space: O(n) + O(s) + O(r) --> O(n + k) where k <= n always --> O(n)


# Based on performance tests, duSort2 eclipses TimSort's performance when less than 5% of input is unique.
# When all input is unique, duSort2 runs ~ 10 times slower than TimSort
def duSort2(a: list):
    i = 0
    count_nums = dict()
    # Runtime building count_nums: O(n)
    # Space Complexity: O(k) where k is the number of
    # distinct elements within our input a
    # By definition, k <= n
    for elem in a:
        if elem in count_nums:
            count_nums[elem] += 1
        else:
            count_nums[elem] = 1
    # Runtime creating the sorted count array: O(n)
    # Space Complexity: O(1)
    for key in sorted(set(a)):  # The python sorted() method takes O(k*log(k)) with space O(k)
        while count_nums[key]:
            a[i] = key
            i += 1
            count_nums[key] -= 1
    return a
    # Total runtime: O(n) + O(k*log(k)) + O(n) --> O(n) + O(k*log(k)) --> O(n + k*log(k))
    # Total space: O(k) where k <= n always --> O(n) worst case, O(k) average/best


def benchmark(a: list):
    aux: list = []
    aux_alph: list = []
    for num in a:
        if num.lstrip('-').isdigit() or num.replace('.', '').isdigit():
            aux.append(float(num))
        else:
            aux_alph.append(num)
    a = sorted(aux).append(sorted(aux_alph))
    return a


def benchmark2(a: list):
    return sorted(a)


# Basic main function for testing and debugging. Not critical to the algorithm
if __name__ == '__main__':
    with open('input3.txt', 'r') as f:
        data = f.read()
        data = data.split()
    cProfile.run('benchmark(data)')
    cProfile.run('benchmark2(data)')
    cProfile.run('duSort(data)')
    cProfile.run('duSort2(data)')
    #data = duSort(data)
    #print(data)
