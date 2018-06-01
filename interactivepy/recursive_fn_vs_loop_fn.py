def req_sum(num):
    total_sum = 0
    if len(num) == 1:
        #print("if: ", num)
        total_sum += num[0]
    elif len(num) > 1:
        #print("elif: ", num)
        total_sum += req_sum(num[0:1]) + req_sum(num[1:])
    return total_sum


def loop_sum(num):
    total_sum = 0
    for n in num:
        total_sum += n
    return total_sum


def req_factorial(n):
    multi = 1
    if n <= 1:
        multi = 1
    elif n > 1:
        multi = n * req_factorial(n - 1)
    return multi


def loop_factorial(n):
    multi = 1
    for m in range(n):
        multi = multi * (m + 1)
    return multi


timeit.timeit(setup='gc.disable(); from __main__ import req_sum',
              stmt='req_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])', number=1)
timeit.timeit(setup='gc.disable(); from __main__ import loop_sum',
              stmt='loop_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])', number=1)
timeit.timeit(setup='gc.disable(); from __main__ import req_factorial',
              stmt='req_factorial(100)', number=1)
timeit.timeit(setup='gc.disable(); from __main__ import loop_factorial',
              stmt='loop_factorial(100)', number=1)
