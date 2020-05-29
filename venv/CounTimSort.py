# Combined complexity of improved count sort algorithm:
# For the purpose of analysis, k is the number of unique values numeric values in our input,
# and r is the number of Non-numeric values in our input
# Runtime Complexity: O(n + k*log(k) + r*log(r))
# O(n) best for sufficiently small k, O(n + k*log(k) + r*log(r)) average,
# O(n*log(n)) worst when every value in our input is either unique or a Non-numeric value.
# Space Complexity: O(n) best/average/worst. Technically O(k + n) but k <= n always, reduces to O(n)

# Note that this count sort handles positive/negative floats/integers.
# Non-float input is sorted using TimSort (alphabetically)

# This variant has worse average case than pure duSort, but can sort non-integer input alphabetically.

# Since this algorithm is composed of count sort combined with TimSort, it is stable,
# meaning that same-value input maintains its order as output.

base = 35

def duTimSort(a: list):
    prev_val = 0
    curr = 0
    aux = []
    aux_num = []
    aux_alph = []
    count_nums = dict()
    # Runtime for copying input array: O(n)
    # Space complexity: 0(n)
    for num in a:
        if num.lstrip('-').isdigit() or num.replace('.', '').isdigit():
            aux_num.append(float(num))
        else:
            aux_alph.append(num)
    # Runtime building count_nums: O(n)
    # Space Complexity: O(k) where k is the number of
    # distinct numbers within our input a
    # By definition, k <= n
    for num in aux_num:
        if num in count_nums.keys():
            count_nums[num] += 1
        else:
            count_nums[num] = 1
    # Runtime adjusting count_nums to contain output positions: O(k) where k <= n
    # Space Complexity: O(1)
    for key in sorted(count_nums.keys()): # The python sorted() method takes O(k*log(k)) with space O(k)
        curr = count_nums[key] - 1
        count_nums[key] = count_nums[key] + prev_val
        prev_val = count_nums[key]
        count_nums[key] -= curr
    # Runtime creating the sorted count array: O(n)
    # Space Complexity: O(1)
    for i, num in enumerate(a):
        if num.lstrip('-').isdigit() or num.replace('.', '').isdigit():
            aux_num[count_nums[float(num)] - 1] = a[i]
            count_nums[float(num)] += 1
    # Use TimSort for non numeric data. Runtime: O(r*log*(r)) where r is the number of non-numeric data points
    # Space complexity: O(r)
    aux_alph = sorted(aux_alph)
    # Runtime copying the sorted info back: O(n)
    # Space Complexity: O(1)
    aux = aux_num + aux_alph
    for i, num in enumerate(aux):
        a[i] = num
    return a
    # Total runtime: O(n) + O(n) + O(k) + O(k*logk) + O(n) --> O(3n) + O(2k*logk) --> O(n + k*logk)
    # Total space: O(n) + O(k) + O(1) + O(1) --> O(n + k) + 2 where k <= n always --> O(n)

# Basic main function for testing and debugging. Not critical to the algorithm
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
        data = data.split()
    data = duSort(data)
    print(data)

