"""
    입력.
    t = 1 ~ t = n 까지
    주식값들이 들어온다.

    출력.
    최대이익 시점 b, s를 출력
    단, 최대이익이 같으면 b가 더 큰값, b가 같으면 s가 더 작은 값

    
"""
data = list()
with open('4주차과제/sampleData4/3.inp', 'r') as f:
    data = [int(val) for val in f.readlines()]

print(data)
best = 0
min_time = 0; max_time = len(data)
for i in range(max_time-1, -1, -1):
    for j in range(0, i):
        if best < data[i] - data[j]:
            best = data[i] - data[j]
            min_time = j
            max_time = i
        elif best == data[i] - data[j]:
            if i < max_time:
                max_time = i
            if j > min_time:
                min_time = j

print(best)
print(min_time, max_time)


# with open('4주차과제/sampleData4/allin.out', 'w') as f:
#     f.write(str(min_time)+' '+str(max_time))