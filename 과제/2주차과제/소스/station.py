"""
    1. 입력 -> a좌표, b좌표, p좌표
    2. 케이스 분류
    3. 출력 -> 최소거리
"""
import math

coo_a = list()
coo_b = list()
coo_p = list()

# with open('./sampleData2/2.inp', 'r') as f:
with open('./station.inp', 'r') as f:
    for a in f.readline().split():
        coo_a.append(int(a))
    for b in f.readline().split():
        coo_b.append(int(b))
    for p in f.readline().split():
        coo_p.append(int(p))

# print('coo_a = ', coo_a)    
# print('coo_b = ', coo_b)
# print('coo_p = ', coo_p)

# 좌표 거리 계산
def dist(coo1, coo2):
    distance = ((coo1[0] - coo2[0])**2 + (coo1[1] - coo2[1])**2 + (coo1[2] - coo2[2])**2)**0.5
    return distance

# 선분 위 점
def onLine(coo_a, coo_b, t) :
    return [t*coo_b[0] + (1-t)*coo_a[0], t * coo_b[1] + (1-t) * coo_a[1], t * coo_b[2] + (1-t) * coo_a[2] ]

# 케이스 분류
AB = (dist(coo_a, coo_b))
AP = (dist(coo_a, coo_p))
BP = (dist(coo_b, coo_p))

if BP**2 >= AB**2 + AP**2:
    min = AP
elif AP**2 >= AB**2 + BP**2:
    min = BP
else :
    while AP != BP:
        if AP > BP:
            coo_a = onLine(coo_a, coo_b, 0.5)
            AP = dist(coo_a, coo_p)
        else:
            coo_b = onLine(coo_a, coo_b, 0.5)
            BP = dist(coo_b, coo_p)
    
    # AP == BP
    mid = onLine(coo_a, coo_b, 0.5)
    min = dist(mid, coo_p)

min = math.ceil(min)
# print(min)

with open('./station.out', 'w') as f:
    f.write(str(min))


    
