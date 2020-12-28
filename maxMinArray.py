def solve(arr):
    ans = []

    while len(arr) > 0:
        max_val = max(arr)
        min_val = min(arr)
        ans.append(max_val)
        arr.remove(max_val)
        if len(arr) > 1:
            ans.append(min_val)
            arr.remove(min_val)

    return ans


print(solve([9, 1, 8, 2, 7, 3, 6, 4, 4, 4]))
