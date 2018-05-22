
def ord_seq_graph(seq):
    for e in seq:
        if type(e) is int and e > 0:
            pass
        else:
            print("sequence has to be of positive integers!")
            return
    try:
        if sum(seq)%2 == 0:
            seq.sort(reverse=True)
            print("start_seq: ", seq)
            seq_lenght = len(seq)
            for i in range(seq_lenght):
                deg = seq.pop(0)
                print("i: ", i)
                print("deg: ", deg)
                j = 0
                if deg <= len(seq):
                    while j < deg:
                        if seq[j] > 0:
                            seq[j] -= 1
                            j += 1
                        else:
                            print("One of the neighbours degree is already 0!: ", seq[j])
                            return seq
                    seq.sort(reverse=True)
                    if sum(seq)%2 != 0:
                        print("Sum of degrees is not an even number: ", sum(seq))
                        return seq
                    else:
                        print("seq: ", seq)
                else:
                    print("Degree of first vertex is bigger then number of the possible neighbours: ", deg, " , ", len(seq))
                    return seq
            print("The list can be a simple graph!")
            return seq
        else:
            print("Sum of degrees is not even number - (sum, sum%2): ", sum(seq), " , ", sum(seq)%2)
    except:
        print("Not a graph sequence! Vertex degrees have to be non negative integers and the sum of them should be even number!")


