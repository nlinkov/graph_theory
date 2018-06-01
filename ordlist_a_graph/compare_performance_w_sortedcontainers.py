
import timeit
from sortedcontainers import SortedList
import heapq

# use sort() method on list


def ord_seq_graph(seq):
    for e in seq:
        if type(e) is int and e > 0:
            pass
        else:
            print("sequence has to be of positive integers!")
            return
    try:
        if sum(seq) % 2 == 0:
            seq.sort(reverse=True)
            seq_lenght = len(seq)
            for i in range(seq_lenght):
                deg = seq.pop(0)
                j = 0
                if deg <= len(seq):
                    while j < deg:
                        if seq[j] > 0:
                            seq[j] -= 1
                            j += 1
                        else:
                            print("One of the neighbours degree is already 0!: ")
                            return
                    seq.sort(reverse=True)
                    if sum(seq) % 2 != 0:
                        print("Sum of degrees is not an even number: ")
                        return
                else:
                    print("Degree of first vertex is bigger then number of the possible neighbours: ")
                    return
            print("The list can be a simple graph!")
            return
        else:
            print("Sum of degrees is not even number!")
    except:
        print("Not a graph sequence! Vertex degrees have to be non negative integers and the sum of them should be even number!")
        return

# use sortedcontainers module - SortedList


def ord_seq_graph2(seq):
    sl = SortedList(seq)
    for e in iter(sl):
        if type(e) is int and e > 0:
            pass
        else:
            print("sequence has to be of positive integers!")
            return
    try:
        if sum(sl) % 2 == 0:
            seq_lenght = len(sl)
            for i in range(seq_lenght):
                deg = sl.pop()
                if deg <= len(sl):
                    sl = SortedList([(n - 1)
                                     for n in iter(sl[(len(sl) - deg):])] + sl[:(len(sl) - deg)])
                    if sum(sl) % 2 != 0:
                        print("Sum of degrees is not an even number: ")
                        return
                else:
                    print("Degree of first vertex is bigger then number of the possible neighbours: ")
                    return
            print("The list can be a simple graph!")
            return
        else:
            print("Sum of degrees is not even number!")
            return
    except:

        print("Not a graph sequence! Vertex degrees have to be non negative integers and the sum of them should be even number!")
        return

# Using heapq for sorting. Reversing by negative integers!!!


def ord_seq_graph3(orig_seq):
    seq = []
    for e in orig_seq:
        if type(e) is int and e > 0:
            heapq.heappush(seq, -e)
        else:
            print("sequence has to be of positive integers!")
            return
    try:
        if sum(seq) % 2 == 0:
            seq_lenght = len(seq)
            for i in range(seq_lenght):
                deg = heapq.heappop(seq)
                if -(deg) <= len(seq):
                    seq_mid = []
                    for j in range(-deg):
                        if -seq[0] > 0:
                            seq_mid.append(heapq.heappop(seq))
                        else:
                            print("One of the neighbours degree is already 0!: ")
                            return
                    for k in seq_mid:
                        heapq.heappush(seq, k + 1)
                    if sum(seq) % 2 != 0:
                        print("Sum of degrees is not an even number: ")
                        return
                else:
                    print("Degree of first vertex is bigger then number of the possible neighbours: ")
                    return
            print("The list can be a simple graph!")
            return
        else:
            print("Sum of degrees is not even number!")
    except:
        print("Not a graph sequence! Vertex degrees have to be non negative integers and the sum of them should be even number!")
        return


def ord_seq_graph5(seq):
    sl = SortedList(seq)
    for e in iter(sl):
        if type(e) is int and e > 0:
            pass
        else:
            print("sequence has to be of positive integers!")
            return
    try:
        if sum(sl) % 2 == 0:
            seq_lenght = len(sl)
            for i in range(seq_lenght):
                deg = sl.pop()
                if deg <= len(sl):
                    sl.update([(sl.pop() - 1) for n in range(deg)])
                    if sum(sl) % 2 != 0:
                        print("Sum of degrees is not an even number: ")
                        return
                else:
                    print("Degree of first vertex is bigger then number of the possible neighbours: ")
                    return
            print("The list can be a simple graph!")
            return
        else:
            print("Sum of degrees is not even number!")
            return
    except:
        print("Not a graph sequence! Vertex degrees have to be non negative integers and the sum of them should be even number!")
        return


timeit.timeit(setup='gc.disable(); from __main__ import ord_seq_graph',
              stmt='ord_seq_graph([3,3,4,4,4,4,4,5,5,7,8,9,10,7,7,8,7,6,8,11,1,2,3,4,5,5,1,2,3,4,5,7,3,3,4,4,4,4,4,5,5,7,8,9,10,7,7,8,7,6,8,11,1,2,3,4,5,5,1,2,3,4,5,7])', number=1)
timeit.timeit(setup='gc.disable(); from __main__ import ord_seq_graph2',
              stmt='ord_seq_graph2([3,3,4,4,4,4,4,5,5,7,8,9,10,7,7,8,7,6,8,11,1,2,3,4,5,5,1,2,3,4,5,7,3,3,4,4,4,4,4,5,5,7,8,9,10,7,7,8,7,6,8,11,1,2,3,4,5,5,1,2,3,4,5,7])', number=1)
timeit.timeit(setup='gc.disable(); from __main__ import ord_seq_graph3',
              stmt='ord_seq_graph3([3,3,4,4,4,4,4,5,5,7,8,9,10,7,7,8,7,6,8,11,1,2,3,4,5,5,1,2,3,4,5,7,3,3,4,4,4,4,4,5,5,7,8,9,10,7,7,8,7,6,8,11,1,2,3,4,5,5,1,2,3,4,5,7])', number=1)
timeit.timeit(setup='gc.disable(); from __main__ import ord_seq_graph5',
              stmt='ord_seq_graph5([3,3,4,4,4,4,4,5,5,7,8,9,10,7,7,8,7,6,8,11,1,2,3,4,5,5,1,2,3,4,5,7,3,3,4,4,4,4,4,5,5,7,8,9,10,7,7,8,7,6,8,11,1,2,3,4,5,5,1,2,3,4,5,7])', number=1)
