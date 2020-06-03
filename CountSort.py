# Combined complexity of improved count sort algorithm:
# For the purpose of analysis, k is the number of unique values in our input,
# r is the number of unique Non-numeric values in our input,
# and s is the number of unique numeric values in our input. By definition, r + s = k
# Runtime Complexity: O(n + k*log(k))
# O(n) best for sufficiently small k, O(n + k*log(k)) average,
# O(n*log(n)) worst when every value in our input is unique.
# Space Complexity: O(n) best/average/worst. Technically O(k + n) but k <= n always, reduces to O(n)

# Note that this count sort handles positive/negative floats/integers, symbols, and character input.

# Since this algorithm is composed of count sort combined with TimSort, it is stable,
# meaning that same-value input maintains its order as output.

base = 35

def duSort(a: list):
    prev_val = 0
    curr = 0
    aux = []
    aux_alph = []
    count_nums = dict()
    count_nums_aux = dict()
    # Runtime for copying input array: O(n)
    # Space complexity: 0(n)
    for num in a:
        if num.lstrip('-').isdigit() or num.replace('.', '').isdigit():
            aux.append(float(num))
        else:
            aux_alph.append(num)
    # Runtime building count_nums: O(s)
    # Space Complexity: O(s) where s is the number of
    # distinct numeric elements within our input a
    # By definition, s <= k
    for num in aux:
        if num in count_nums.keys():
            count_nums[num] += 1
        else:
            count_nums[num] = 1
    # Runtime building count_nums: O(r)
    # Space Complexity: O(r) where r is the number of
    # distinct non numeric elements within our input a
    # By definition, r <= k
    for elem in aux_alph:
        if elem in count_nums.keys():
            count_nums_aux[elem] += 1
        else:
            count_nums_aux[elem] = 1
    # Runtime adjusting count_nums to contain output positions: O(s) where s <= k
    # Space Complexity: O(1)
    for key in sorted(count_nums.keys()): # The python sorted() method takes O(s*log(s)) with space O(s)
        curr = count_nums[key] - 1
        count_nums[key] = count_nums[key] + prev_val
        prev_val = count_nums[key]
        count_nums[key] -= curr
    # Runtime adjusting count_nums to contain output positions: O(r) where r <= k
    # Space Complexity: O(1)
    prev_val = 0
    for key in sorted(count_nums_aux.keys()):  # The python sorted() method takes O(r*log(r)) with space O(r)
        curr = count_nums_aux[key] - 1
        count_nums_aux[key] = count_nums_aux[key] + prev_val
        prev_val = count_nums_aux[key]
        count_nums_aux[key] -= curr
    # Runtime creating the sorted count array: O(n)
    # Space Complexity: O(1)
    for i, num in enumerate(a):
        if num.lstrip('-').isdigit() or num.replace('.', '').isdigit():
            aux[count_nums[float(num)] - 1] = a[i]
            count_nums[float(num)] += 1
        else:
            aux_alph[count_nums_aux[num] - 1] = a[i]
            count_nums_aux[num] += 1
    # Runtime copying the sorted info back: O(n)
    # Space Complexity: O(1)
    aux += aux_alph
    for i, num in enumerate(aux):
        a[i] = num
    return a
    # Total runtime: O(n) + O(s*logs) + O(r*logr) --> O(n) + O(k*logk) --> O(n + k*logk)
    # Total space: O(n) + O(s) + O(r) --> O(n + k) where k <= n always --> O(n)

# Basic main function for testing and debugging. Not critical to the algorithm
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
        data = data.split()
    data = duSort(data)
    print(data)

