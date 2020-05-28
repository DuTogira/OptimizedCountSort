# Combined complexity of improved count sort algorithm:
# Runtime Complexity: O(n) best, O(n + k*log(k)) average, O(n*log(n)) worst when k == n
# Space Complexity: O(n) best/average/worst
# Note that for the purpose of analysis, k is the number of distinct values in our input

# Note that this count sort handles positive/negative floats, characters, and symbols.
# Non-float characters are sorted based on their ASCII integer value.

# Since this algorithm is composed of count sort combined with TimSort, it is stable,
# meaning that same-value input maintains its order as output.

base = 35

def duSort(a):
    # Runtime for copying input array: O(n)
    # Space complexity copying input array: 0(n)
    aux = []
    for num in a:
        if num.lstrip('-').isdigit() or num.replace('.', '').isdigit():
            aux.append(float(num))
        else:
            aux.append(sum(int(c) if c.isdigit() else ord(c) for c in num))
    count_nums = dict()
    # Runtime building count_nums: O(n)
    # Space Complexity: O(k) where k is the number of
    # distinct numbers within our input a
    # By definition, k <= n
    for num in aux:
        if num in count_nums.keys():
            count_nums[num] += 1
        else:
            count_nums[num] = 1
    # Runtime adjusting count_nums to contain output positions: O(k) where k <= n
    # Space Complexity: O(1)
    prev_val = 0
    curr = 0
    # The python sorted() method takes O(k*log(k))
    for key in sorted(count_nums.keys()):
        curr = count_nums[key] - 1
        count_nums[key] = count_nums[key] + prev_val
        prev_val = count_nums[key]
        count_nums[key] -= curr
    # Runtime creating the sorted count array: O(n)
    # Space Complexity: O(1)
    for i, num in enumerate(a):
        if num.lstrip('-').isdigit() or num.replace('.', '').isdigit():
            aux[count_nums[float(num)] - 1] = a[i]
            count_nums[float(num)] += 1
        else:
            aux[count_nums[sum(int(c) if c.isdigit() else ord(c) for c in num)] - 1] = a[i]
            count_nums[sum(int(c) if c.isdigit() else ord(c) for c in num)] += 1
    a = aux
    return a

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
        data = data.split()
    data = duSort(data)
    print(data)

