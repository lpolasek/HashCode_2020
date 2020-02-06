import sys

def calc(l):
    global p
    global sli
    global scor
    global bScor
    global bSli

    for j in range(l,-1,-1):
        if (scor + p[j]) > M:
            continue
        scor += p[j]
        sli.append(j)

    if scor > bScor:
        bScor = scor
        bSli = sli[:]

    return bScor

bScor = 0
bSli = []
M, N = ( int(x) for x in sys.stdin.readline().split(' '))
p = [int(x) for x in sys.stdin.readline().split(' ')]

for i in range(N-1,-1,-1):
    scor = 0
    sli = []

    if calc(i) == M:
        break

    while sli:
        lst = sli.pop()
        scor -= p[lst]
        if calc(lst-1,) == M:
            break

#print(bScor)
print(len(bSli))
bSli.reverse()
print(' '.join([ str(i) for i in bSli]))

