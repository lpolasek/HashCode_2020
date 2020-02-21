import sys
import math
from collections import namedtuple
from functools import reduce

Library = namedtuple('Library','id,days,bk_shp,bks,best')
class Book:
    id=0
    score=0
    def __init__(self, i, s):
        self.id=i
        self.score=s

    def __str__(self):
        return "Book(id=%d score=%d)" % (self.id, self.score)

B,L,D = (int(x) for x in sys.stdin.readline().rstrip().split())
books = [Book(int(x[0]),int(x[1])) for x in enumerate(sys.stdin.readline().rstrip().split())]

libraries = []
for i in range(L):
    N,T,M = (int(x) for x in sys.stdin.readline().rstrip().split())
    bks = [books[int(x)] for x in sys.stdin.readline().rstrip().split()]
    bks.sort(key=(lambda x: (-x.score)))
    libraries.append(Library(i,T,M,bks,bks[0].score))

libraries.sort(key=(lambda x: (x.days,-x.bk_shp,-x.best)))

# save libraries with all books already scanned to put them at the end
emptys=[]

print(L)
day=0
for l_ in range(L):
    l = libraries.pop(0)
    day  += l.days

    # If all books of the library already scanned
    # list it at the end
    if reduce(lambda y,z:y+z.score, l.bks,0) == 0:
        emptys.append(l)
        continue
    print(l.id, len(l.bks))
    bks = sorted(l.bks, key=(lambda x: (-x.score)))
    print(' '.join([str(x.id) for x in bks]))
    # All books scanned gets 0 score
    for b in enumerate(bks):
        if day+(math.floor(b[0]/l.bk_shp)) <= D-1:
            b[1].score = 0

for l in emptys:
    print(l.id, len(l.bks))
    bks = sorted(l.bks, key=(lambda x: (-x.score)))
    print(' '.join([str(x.id) for x in bks]))
