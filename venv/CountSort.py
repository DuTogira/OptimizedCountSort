# Combined complexity of improved count sort algorithm:
# Runtime Complexity: O(n) best, O(n + k*log(k)) average, O(n*log(n)) worst when k == n
# Space Complexity: O(n) best/average/worst

# Note that this count sort handles negative integers, characters, and symbols.
# This algorithm will not handle non-integer numbers correctly, though it technically sorts them

# Since this algorithm is composed of count sort combined with TimSort, it is stable

base = 35

def duSort(a):
    # Runtime for copying input array: O(n)
    # Space complexity copying input array: 0(n)
    aux = []
    for num in a:
        if num.lstrip('-').isdigit():
            aux.append(int(num))
        elif num.isalnum():
            aux.append(int(num, base))
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
    # The python sorted() method takes O(k*log(k))... need to find a way to reduce this
    for key in sorted(count_nums.keys()):
        count_nums[key] = count_nums[key] + prev_val
        prev_val = count_nums[key]
    # Runtime creating the sorted count array: O(n)
    # Space Complexity: O(1)
    i = 0
    for num in a:
        if num.lstrip('-').isdigit():
            aux[count_nums[int(num)] - 1] = a[i]
            count_nums[int(num)] -= 1
        elif num.isalnum():
            aux[count_nums[int(num, base)] - 1] = a[i]
            count_nums[int(num, base)] -= 1
        else:
            aux[count_nums[sum(int(c) if c.isdigit() else ord(c) for c in num)] - 1] = a[i]
            count_nums[sum(int(c) if c.isdigit() else ord(c) for c in num)] -= 1
        i += 1
    a = aux
    return a

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
        data = data.split()
    data = duSort(data)
    print(data)

