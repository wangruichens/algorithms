def partition(xs, start, end):
    follower = leader = start
    while leader < end:
        if xs[leader] <= xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1
    xs[follower], xs[end] = xs[end], xs[follower]
    return follower


def _quicksort(xs, start, end, k):
    if start >= end:
        return
    p = partition(xs, start, end)
    if p <= k:
        # _quicksort(xs, start, p - 1)
        _quicksort(xs, p + 1, end, k - p - 1)
    if p > k:
        _quicksort(xs, start, p - 1, k)
        # _quicksort(xs, p + 1, end)


def quicksort(xs):
    _quicksort(xs, 0, len(xs) - 1, 4)


import random

a = [random.randint(0, 15) for i in range(10)]
quicksort(a)
print(a)
