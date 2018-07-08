def ord_seq_graph4(orig_seq):
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
                if sum(seq) % 2 != 0:
                    print("Sum of degrees is not an even number: ")
                    return
                deg = heapq.heappop(seq)
                if -(deg) <= len(seq):
                    for j in range(-deg):
                        seq[j] += 1
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
