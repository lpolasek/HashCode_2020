import sys

M, N = ( int(x) for x in sys.stdin.readline().split(' '))
p = [int(x) for x in sys.stdin.readline().split(' ')]

bScor = 0
bSli = []

for i in range(N-1,-1,-1):
    scor = 0
    sli = []

    for j in range(i,-1,-1):
        if (scor + p[j]) > M:
            continue
        scor += p[j]
        sli += [j]

    if scor > bScor:
        bScor = scor
        bSli = sli[:]


    if bScor == M:
        break

    while sli:
        lst = sli.pop()
        scor -= p[lst]
        for j in range(lst-1,-1,-1):
            if (scor + p[j]) > M:
                continue
            scor += p[j]
            sli += [j]

        if scor > bScor:
            bScor = scor
            bSli = sli[:]

        if bScor == M:
            break

#print(bScor)
print(len(bSli))
bSli.reverse()
print(' '.join([ str(i) for i in bSli]))

