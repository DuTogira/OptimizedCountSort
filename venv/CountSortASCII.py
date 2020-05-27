from collections import OrderedDict

# Combined complexity of improved count sort algorithm:
# Runtime Complexity: O(n) best, O(n + k*log(k)) average, O(n*log(n)) worst when k == n
# Space Complexity: O(n) best/average/worst

# This count sort handles all ASCII characters, but will not properly handle
# negative integers, as the negative sign is seen as a character

# Since this algorithm is composed of count sort combined with TimSort, it is stable

def pickingNumbers(a):
    biggest = a[0]
    smallest = a[0]
    # Runtime for copying input array: O(n)
    # Space complexity copying input array: 0(n)
    aux = []
    for num in a:
        aux.append(int(''.join(str(ord(c)) for c in num)))
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
        aux[count_nums[int(''.join(str(ord(c)) for c in num))] - 1] = a[i]
        count_nums[int(''.join(str(ord(c)) for c in num))] -= 1
        i += 1
    a = aux
    return a

if __name__ == '__main__':
    with open('input2.txt', 'r') as f:
        data = f.read()
        data = data.split()
    data = pickingNumbers(data)
    print(data)

