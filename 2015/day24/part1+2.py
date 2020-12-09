import functools
import operator


def qe(l):
    return functools.reduce(operator.mul, l)


def get_all_subsets_with_sum_rec(dp, arr, idx, val, cur_arr):
    result_list = []
    # reached the end and what's left is the first element
    if idx == 0 and val != 0 and dp[0][val]:
        cur_arr.append(idx)
        subset = [arr[i] for i in cur_arr]
        cur_arr_s = set(cur_arr)
        left = [arr[i] for i in range(len(arr)) if i not in set(cur_arr_s)]
        result_list.append((subset, left))
        return result_list
    # reached the end
    if idx == 0 and val == 0:
        subset = [arr[i] for i in cur_arr]
        cur_arr_s = set(cur_arr)
        left = [arr[i] for i in range(len(arr)) if i not in set(cur_arr_s)]
        result_list.append((subset, left))
        return result_list
    # sum can be done without current elem
    if dp[idx-1][val]:
        cur_arr_c = cur_arr.copy()
        result_list += get_all_subsets_with_sum_rec(dp, arr, idx-1, val, cur_arr_c)
    # sum can be done considering the current elment
    if arr[idx] <= val and dp[idx-1][val - arr[idx]]:
        cur_arr.append(idx)
        result_list += get_all_subsets_with_sum_rec(dp, arr, idx-1, val-arr[idx], cur_arr)
    return result_list


def compute_dp_matrix(arr, val):
    dp = [[True] + [False for _ in range(val)] for __ in range(len(arr))]
    if arr[0] <= val:
        dp[0][arr[0]] = True
    for i in range(1, len(arr)):
        for j in range(0, val + 1):
            if arr[i] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp


def get_all_subsets_with_sum(arr, val):
    dp = compute_dp_matrix(arr, val)
    # no such subset
    if not dp[len(arr) - 1][val]:
        return []
    return get_all_subsets_with_sum_rec(dp, arr, len(arr) - 1, val, [])


def can_be_split(arr, partitions):
    val = sum(arr) // partitions
    if partitions == 2:
        dp = compute_dp_matrix(arr, val)
        return dp[len(arr) - 1][val]
    for subset, left in get_all_subsets_with_sum(arr, val):
        if can_be_split(left, partitions-1):
            return True
    return False


def find_best_partition(weights, partitions):
    m = mqe = float('inf')
    part = None
    res = get_all_subsets_with_sum(weights, sum(weights) // partitions)
    min_len = len(min(res, key=lambda x: len(x[0]))[0])
    for a, left in res:
        if len(a) > min_len:
            continue
        if can_be_split(left, partitions - 1):
            if len(a) < m or (len(a) == m and qe(a) < mqe):
                m = len(a)
                mqe = qe(a)
                part = (a, left)
    return m, mqe, part


weights = list(map(int, open('in').read().split('\n')))

# part 1
print(find_best_partition(weights, 3))

# part 2
print(find_best_partition(weights, 4))
