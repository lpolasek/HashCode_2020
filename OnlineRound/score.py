"""
Check score of an output file

Usage:
    cat f_libraries_of_the_world.txt f_libraries_of_the_world.out | python3 score.py
"""
import sys
import math
from collections import namedtuple
from functools import reduce

class Library:
    id=0
    days=0
    bk_shp=0
    bks=[]
    best=0
    used=False
    def __init__(self, id, days, bk_shp, bks,  best):
        self.id=id
        self.days=days
        self.bk_shp=bk_shp
        self.bks=bks
        self.best=best
    def __str__(self):
        return "Library(id=%d days=%d bks/day=%d bksCnt=%d)" % (self.id, self.days, self.bk_shp, len(self.bks))

class Book:
    id=0
    score=0
    libraries=[]
    def __init__(self, i, s):
        self.id=i
        self.score=s
    def __str__(self):
        return "Book(id=%d score=%d)" % (self.id, self.score)

def fillDays(days, lib, day, D):
    d = 0
    while (d + day + lib.days) < D:
        bg = d * lib.bk_shp
        nd = (d+1) * lib.bk_shp
        for l in lib.bks[bg:nd]:
            days[d + day + lib.days] += [books[l].score]
            books[l].score = 0
        d += 1

B,L,D = (int(x) for x in sys.stdin.readline().rstrip().split())
books = [Book(int(x[0]),int(x[1])) for x in enumerate(sys.stdin.readline().rstrip().split())]

libraries = []
for i in range(L):
    N,T,M = (int(x) for x in sys.stdin.readline().rstrip().split())
    bks = [books[int(x)] for x in sys.stdin.readline().rstrip().split()]
    library = Library(i,T,M,bks,bks[0].score)
    libraries.append(library)

line = ''
while len(line) == 0:
    line = sys.stdin.readline().rstrip()
scL = int(line)
scLibs = []
for i in range(scL):
    scLibId, scLibLen = (int(x) for x in sys.stdin.readline().rstrip().split())
    # check if library exists
    if scLibId >= L:
        print("Invalid library %d" % scLibId)
        sys.exit(0)
    scLibBks = [int(x) for x in sys.stdin.readline().rstrip().split()]
    scLibT = libraries[scLibId].days
    scLibM = libraries[scLibId].bk_shp
    scLibs.append(Library(scLibId, scLibT, scLibM, scLibBks, 0))

# Check all libraries has correct books
for lib in scLibs:
    bk_ids = list(map(lambda b: b.id,libraries[lib.id].bks))
    for bk in lib.bks:
        if bk not in bk_ids:
            print("Book %d not found in library %d" % (bk, lib.id))
            sys.exit(0)

# Compute the total
days = []
for d in range(D):
    days.append([])
day = 0

for lib in scLibs:
    # should fill days with scores
    fillDays(days, lib, day, D)
    day += lib.days

# for l in libraries:
#     print(l)
# print()

# for d in enumerate(days):
#     print(d[0], d[1])

score = sum(map(lambda d: sum(d), days))
print('Score: %d' % score)
