def third_largest_v1(lst):
    if len(set(lst)) < 3:
        return None
    return sorted(set(lst))[-3]

def third_largest_v2(lst):
    if len(lst) < 3:
        return None

    first = second = third = float('-inf')
    
    for num in lst:
        if num > first:
            first, second, third = num, first, second
        elif first >= num >= second:
            second, third = num, second
        elif second >= num >= third:
            third = num

    return third

import heapq
def third_largest(lst):
    if len(lst) < 3:
        return None
    return heapq.nlargest(3, lst)[-1]

print(third_largest_v1([10, 20, 4, 45, 99]))
print(third_largest_v1([3, 2, 1]))
print(third_largest_v1([3, 3, 3, 3, 3]))
print(third_largest_v1([1, 2]))

print(third_largest_v2([10, 20, 4, 45, 99]))
print(third_largest_v2([3, 2, 1]))
print(third_largest_v2([3, 3, 3, 3, 3]))
print(third_largest_v2([1, 2]))