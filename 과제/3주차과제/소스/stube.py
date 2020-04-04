import math
coo_a = []
coo_b = []
coo_c = []
coo_d = []

with open('stube.inp', 'r') as f:
    A = f.readline().split()
    coo_a = list(map(float, A))
    B = f.readline().split()
    coo_b = list(map(float, B))
    C = f.readline().split()
    coo_c = list(map(float, C))
    D = f.readline().split()
    coo_d = list(map(float, D))

def dist_power(coo1, coo2):
    distance = (coo1[0] - coo2[0])**2 + (coo1[1] - coo2[1])**2 + (coo1[2] - coo2[2])**2
    return distance

# 선분 위 점
def onLine(coo_a, coo_b, t) :
    return [t*coo_b[0] + (1-t)*coo_a[0], t * coo_b[1] + (1-t) * coo_a[1], t * coo_b[2] + (1-t) * coo_a[2] ]

# 선분에서 가장 가까운 점 찾기
def near_point(start, end, point):
    line = dist_power(start, end)
    left = dist_power(start, point)
    right = dist_power(end, point) 

    if right >= line + left:
        return left, start
    elif left >= line + right:
        return right, end
    else :
        while left != right:
            if left > right:
                start = onLine(start, end, 0.5)
                left = dist_power(start, point)
            else:
                end = onLine(start, end, 0.5)
                right = dist_power(end, point)
        T = onLine(start, end, 0.5)
        return dist_power(T, point), T

def isEqual(p1, p2) :
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    z = p1[2] - p2[2]
    return x**2 < 1 and y**2 < 1 and z**2 < 1

line1, T1 = near_point(coo_c, coo_d, coo_a)
line2, T2 = near_point(coo_a, coo_b, T1)

test_line1, a1 = line1, T1
test_line2, b1 = near_point(coo_c, coo_d, coo_b)
test_line3, c1 = near_point(coo_a, coo_b, coo_c)
test_line4, d1 = near_point(coo_a, coo_b, coo_d)

if isEqual(a1, coo_a) or isEqual(b1, coo_b) or isEqual(c1, coo_c) or isEqual(d1, coo_d):
    line1 = 0
else:
    count = 0
    while line1 != line2 :
        if math.sqrt(line1) < 1:
            line1 = 0
            break
        if count % 2 == 0:
            line1, T1 = near_point(coo_c, coo_d, T2)
        else :
            line2, T2 = near_point(coo_a, coo_b, T1)
        count += 1

with open('stube.out', 'w') as f:
    f.write(str(math.ceil(math.sqrt(line1))))