__author__ = 'Reece'
import math


def mean_calc(args):
    tot = 0
    for a in args:
        tot += a
    mean = tot / len(args)
    return mean


def mode_calc(args):
    things = {}
    for i in args:
        if i in things:
            things[i] += 1
        else:
            things[i] = 1
    highest_num = 0
    m = None
    mode = []
    for t in things:
        if things[t] > highest_num:
            highest_num = things[t]
            m = t
        elif things[t] == highest_num:
            mode.append(t)
    mode.append(m)
    return mode


def median_calc(args):
    args = sorted(args)
    mid = (len(args) + 1) / 2
    if mid % 2 == 0:
        median = args[int(mid) - 1]
    else:
        first = args[math.floor(mid) - 1]
        second = args[math.ceil(mid) - 1]
        median = (first + second) / 2
    return median


numbers = (1, 2, 3, 4, 5, 8, 9, 11, 125, 2)
print(mode_calc(numbers), mean_calc(numbers), median_calc(numbers))