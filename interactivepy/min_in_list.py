def min_list(li):
    l = len(li)
    for i in li:
        k = 0
        for j in li:
            if i <= j:
                k += 1
                if k == l:
                    return i
            else:
                break


def min_list2(li):
    min = li[0]
    for i in li:
        if min > i:
            min = i
    return min


timeit.timeit(setup='gc.disable(); from __main__ import min_list',
              stmt='min_list([4,2,3,-1,1,-1,100,-23,4,5,6,-2])', number=1)

timeit.timeit(setup='gc.disable(); from __main__ import min_list2',
              stmt='min_list2([4,2,3,-1,1,-1,100,-23,4,5,6,-2])', number=1)
