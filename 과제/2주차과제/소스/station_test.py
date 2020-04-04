"""
    입력
    1. A좌표
    2. B좌표
    3. P좌표
    
    출력
    거리(정수, 올림값)

    방법
    1. t0, t1/2, t1값을 비교
    2. case1, 2, 3분류
    3. t0 < t1/2 < t1 => t0일때 최소거리
    4. t1/2 < t0, t1 => 0 < t < 1일 때 최소거리
    5. t1 < t1/2 < t0 => t1일 때 최소거리

    거리
    ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5
    
    올림
    import math
    math.ceit(값)
"""
import math
import numpy
cop_A = []
cop_B = []
cop_P = []
with open('./station.inp', 'r') as f:
#with open('./station.inp', 'rt', encoding='UTF8') as f:
    for a in f.readline().split():
        cop_A.append(int(a)) 
    for b in f.readline().split():
        cop_B.append(int(b))
    for p in f.readline().split():
        cop_P.append(int(p))

def dist(t, p):
    d = ((t[0] - p[0])**2 + (t[1]-p[1])**2 + (t[2]-p[2])**2)**0.5
    return d

def onLine(cop_A, cop_B, t) :
    return [t*cop_B[0] + (1-t)*cop_A[0], t * cop_B[1] + (1-t) * cop_A[1], t * cop_B[2] + (1-t) * cop_A[2] ]

t0 = onLine(cop_A, cop_B, 0)
min = dist(t0, cop_P)

for i in numpy.arange(0, 1.1, 0.01):
    t = onLine(cop_A, cop_B, i)
    if min > dist(t, cop_P):
        min = dist(t, cop_P)

min = math.ceil(min)
# print('min = ', min)

with open('./station.out', 'w') as f:
    f.write(str(min))
    