s1 = ''
for k in range(100000):
    s1 += (random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(100000)).__next__()


def anagramSolution5(s1, s2):
    if (len(s1) and len(s2)) and (sum([ord(n) for n in s1]) == sum([ord(k) for k in s2])):
        return
    else:
        print('not same, sorry!')


def anagramSolution4(s1, s2):
    c1 = [0] * 75
    c2 = [0] * 75

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('0')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('0')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j < 75 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK


timeit.timeit(setup='gc.disable(); from __main__ import anagramSolution1, s1, s2',
              stmt='anagramSolution1(s1,s2)', number=1)
timeit.timeit(setup='gc.disable(); from __main__ import anagramSolution5, s1, s2',
              stmt='anagramSolution5(s1,s2)', number=1)
