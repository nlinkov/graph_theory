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
