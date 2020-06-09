# Combined complexity of improved count sort algorithm:
# For the purpose of analysis, k is the number of unique values in our input,
# n is the number of values in our input,
# k is the number of unique values in our input.
# By definition, k <= n
# Runtime Complexity: O(n + k*log(k))
# O(n) best for sufficiently small k, O(n + k*log(k)) average,
# O(n*log(n)) worst when every value in our input is unique.
# Space Complexity: O(k) best/average. O(n) worst. Technically O(k + n) but k <= n always, reduces to O(n)

# Since this algorithm is composed of count sort combined with TimSort, it is stable,
# meaning that same-value input maintains its order as output.

import cProfile
from random import shuffle


# Based on performance tests, duSort runs ~2 times slower than TimSort, even though its asymptotic run-time is better
# This is because it practically takes as long to build the count dictionaries as it takes for TimSort to sort the data
# Currently duSort becomes competitive with TimSort when < 5% of input data is unique.
def duSort(a: list):
    count_nums = dict()
    # Runtime building count_nums: O(n)
    # Space Complexity: O(k) where k is the number of
    # unique numeric elements within our input a
    # By definition, k <= n
    for i in range(0, len(a)):
        if a[i] in count_nums:
            count_nums[a[i]] += 1
        else:
            count_nums[a[i]] = 1

    i = 0
    # Runtime building output from our count dict: O(n),
    # Space Complexity: O(1)
    for key in sorted(count_nums.keys()):  # sorted runs in O(k * log(k)) --> O(n * log(n)) worst
        for j in range(0, count_nums[key]):
            a[i + j] = key
        i += count_nums[key]
    return a
    # Total runtime: O(n) + O(n) + O(k * log(k)) --> O(n) + O(k*log(k)) --> O(n + k*log(k))
    # Total space: O(k) where k <= n always


def benchmark(a: list):
    aux: list = []
    aux_alph: list = []
    for i in range(0, len(a)):
        try:
            aux.append(float(a[i]))
        except ValueError:
            aux_alph.append(a[i])
    sorted(aux)
    sorted(aux_alph)
    return aux.append(aux_alph)


def duSortTest(a: list):
    aux: list = []
    aux_alph: list = []
    for i in range(0, len(a)):
        try:
            aux.append(float(a[i]))
        except ValueError:
            aux_alph.append(a[i])
    duSort(aux)
    duSort(aux_alph)
    return aux.append(aux_alph)


# Basic main function for testing and debugging. Not critical to the algorithm
if __name__ == '__main__':
    with open('input3.txt', 'r') as f:
        data = f.read()
        data = data.split()
        shuffle(data)
    cProfile.run('benchmark(data)')
    cProfile.run('duSortTest(data)')
    #data = duSortTest(data)
    #print(data)
