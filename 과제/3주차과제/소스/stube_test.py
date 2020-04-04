"""
    입력 
    1. A좌표
    2. B좌표
    3. C좌표
    4. D좌표

    출력
    두 선분 최소 정수길이

    방법
    1. (A,B), (C,D)에서 일단 A에서 (C,D)에 제일 가까운 점 T1을 찾습니다. 
    2. 그 다음 T1에서 선분 (A,B)에있는 제일 가까운 점 T2을 찾습니다. 
    3. T2에서 다시 (C,D)까지의 최단거리점 T3을 구합니다. 
    
    1) T3 == T1
        최소거리 (T1, T2)만세....
    
    2) T3 != T1
        새로운 점 T3라면 다시 T3에서 다른쪽 선분까지의 최단거리점을 구합니다.

    4. 반복
    "왔다리 갔다리" 하면서 짧은 점을 구하는데 그렇게 구한 점의 위치가 변함이 없으면 그게 정답
"""
import math
coo_a = []
coo_b = []
coo_c = []
coo_d = []

with open('3주차과제/sampleData3/3.inp', 'r') as f:
    A = f.readline().split()
    coo_a = list(map(float, A))
    B = f.readline().split()
    coo_b = list(map(float, B))
    C = f.readline().split()
    coo_c = list(map(float, C))
    D = f.readline().split()
    coo_d = list(map(float, D))

print(coo_a, coo_b, coo_c, coo_d)

# 방법
# 1. (A,B), (C,D)에서 일단 A에서 (C,D)에 제일 가까운 점 T1을 찾습니다. 
# 2. 그 다음 T1에서 선분 (A,B)에있는 제일 가까운 점 T2을 찾습니다. 
# 3. T2에서 다시 (C,D)까지의 최단거리점 T3을 구합니다. 

# 1. (A,B), (C,D)에서 일단 A에서 (C,D)에 제일 가까운 선 T1을 찾습니다. 
# 2. 그 다음 T1에서 선분 (A,B)에있는 제일 가까운 점 T2을 찾습니다. 
# 3. T2에서 다시 (C,D)까지의 최단거리점 T3을 구합니다. 

# 좌표 거리 계산
def dist(coo1, coo2):
    distance = ((coo1[0] - coo2[0])**2 + (coo1[1] - coo2[1])**2 + (coo1[2] - coo2[2])**2)**0.5
    return distance

def dist_power(coo1, coo2):
    distance = ((coo1[0] - coo2[0])**2 + (coo1[1] - coo2[1])**2 + (coo1[2] - coo2[2])**2)
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
        print(math.sqrt(dist_power(T, point)))
        return dist_power(T, point), T



# 방법
# 1. (A,B), (C,D)에서 일단 A에서 (C,D)에 제일 가까운 점 T1을 찾습니다. 
line1, T1 = near_point(coo_c, coo_d, coo_a)

# 2. 그 다음 T1에서 선분 (A,B)에있는 제일 가까운 점 T2을 찾습니다. 
line2, T2 = near_point(coo_a, coo_b, T1)

# 3. T2에서 다시 (C,D)까지의 최단거리점 T3을 구합니다.
# 1) T3 == T1
#   최소거리 (T1, T2)만세....
    
# 2) T3 != T1
#   새로운 점 T3라면 다시 T3에서 다른쪽 선분까지의 최단거리점을 구합니다. 
def isEqual(p1, p2) :
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    z = p1[2] - p2[2]
    return x**2 < 1 and y**2 < 1 and z**2 < 1
test_line1, a1 = line1, T1
test_line2, b1 = near_point(coo_c, coo_d, coo_b)
test_line3, c1 = near_point(coo_a, coo_b, coo_c)
test_line4, d1 = near_point(coo_a, coo_b, coo_d)

if isEqual(a1, coo_a) or isEqual(b1, coo_b) or isEqual(c1, coo_c) or isEqual(d1, coo_d):
    print('여기를 거쳤습니다.')
    line1 = 0
else:
    count = 0
    while line1 != line2:
        if math.sqrt(line1) < 2:
            line1 = 0
            break
        if count % 2 == 0:
            line1, T1 = near_point(coo_c, coo_d, T2)
        else :
            line2, T2 = near_point(coo_a, coo_b, T1)
        count += 1

# while line1 != line2:
#     if count % 2 == 0:
#         line1, T1 = near_point(coo_c, coo_d, T2)
#     else :
#         line2, T2 = near_point(coo_a, coo_b, T1)
#     count += 1

print(math.ceil(math.sqrt(0)))
print(math.ceil(math.sqrt(line1)))
with open('3주차과제/소스/answer.out', 'w') as f:
    f.write(str(line1))