def three_sum(nums):
    triplets = set()
    for i in range(len(nums) - 1):
        x = set()
        v1 = nums[i]
        for j in range(i + 1, len(nums)):
            v2 = nums[j]
            y = v1 + v2
            diff = -1 * y
            if (diff in x):
                triplets.add(tuple(sorted([v1, v2, diff])))
                x.remove(diff)
            else:
                x.add(v2)
    return [list(t) for t in triplets]
