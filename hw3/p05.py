def win(nums):
    n = len(nums)
    dp_steps = [None] * (n - 1) + [0]
    dp_next = [None] * (n - 1) + [n - 1]
    def get(i):
        if dp_steps[i] == None:
            reachable_indexes = list(range(i + 1, min(i + nums[i] + 1, n)))
            reachable_indexes = list(map(lambda j: tuple([j, get(j)[1]]), reachable_indexes))


            best_path = min(reachable_indexes, key = lambda x: x[1])
            dp_next[i] = best_path[0]
            dp_steps[i] = best_path[1] + 1

        return dp_next[i], dp_steps[i]

    rounds = 0
    path = []
    cur = 0
    while cur != n - 1:
        cur = get(cur)[0]
        rounds += 1
        path.append(cur)
    return [rounds, path]