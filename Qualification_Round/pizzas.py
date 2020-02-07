import sys

import functools
def check(a):
    global p
    return functools.reduce(lambda a,b : p[b]+a, a, 0)

def calc(l, scor, sli):
    global p
    global bScor
    global bSli

    lscor = 0
    lsli = []

    assert scor == check(sli)
    for j in range(l,-1,-1):
        if (scor + lscor + p[j]) > M:
            continue
        lscor += p[j]
        lsli.append(j)

    if (scor + lscor) > bScor:
        bScor = scor + lscor
        bSli = sli[:] + lsli[:]
        assert bScor == check(bSli)

    return (scor + lscor, sli + lsli, bScor)

bScor = 0
bSli = []
M, N = ( int(x) for x in sys.stdin.readline().split(' '))
p = [int(x) for x in sys.stdin.readline().split(' ')]

for i in range(N-1,-1,-1):
    scor, sli, bScor = calc(i, 0, [])
    if bScor == M:
        break

    while sli:
        lst = sli.pop()
        scor -= p[lst]
        calc(lst-1,scor, sli)
        if bScor == M:
            break

#print(M == bScor, M, bScor)
print(len(bSli))
bSli.reverse()
print(' '.join([ str(i) for i in bSli]))

