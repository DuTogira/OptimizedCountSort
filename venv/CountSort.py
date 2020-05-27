def pickingNumbers(a):
    # Write your code here
    # Combined complexity of algorithm:
    # Runtime Complexity: O(n) best/average, O(k*log(k)) worst
    # Space Complexity: O(n) best/average/worst
    biggest = a[0]
    smallest = a[0]
    # Space complexity copying input array: 0(n)
    aux = a
    # Runtime finding biggest and smallest: O(n)
    # Space complexity: O(1)
    for num in a:
        if num > biggest:
            biggest = num
        if num < smallest:
            smallest = num
    count_nums = dict()
    # Runtime building count_nums: O(n)
    # Space Complexity: O(k) where k is the number of
    # distinct numbers within our input a
    # By definition, k <= n
    for num in a:
        if num in count_nums.keys():
            count_nums[num] += 1
        else:
            count_nums[num] = 1
    big_sum = count_nums[smallest]
    print(count_nums)
    # This sorting takes O(k*log(k))... need to find a way to reduce this
    count_nums = sorted(count_nums)
    # Runtime adjusting count_nums to contain output positions: O(k) where k <= n
    # Space Complexity: O(1)
    prev_val = 0
    for key in count_nums.keys():
        count_nums[key] = count_nums[key] + prev_val
        prev_val = count_nums[key]
    # Runtime creating the sorted count array: O(n)
    # Space Complexity: O(1)
    i = 0
    prev_val = 0
    current_val = 0
    for key in count_nums.keys():
        current_val = count_nums[key]
        while count_nums[key] > prev_val:
            aux[count_nums[key] - 1] = a[i]
            i += 1
        prev_val = current_val
    a = aux
    return a
