"""
    입력.
    t = 1 ~ t = n 까지
    주식값들이 들어온다.

    출력.
    최대이익 시점 b, s를 출력
    단, 최대이익이 같으면 b가 더 큰값, b가 같으면 s가 더 작은 값

   소스/allin_test.py 
   sampleData4/1.inp
"""
data = list()
min_time = 0; max_time = 0
max_value = -99999; min_value = 99999
best = 0
with open('sampleData4/3.inp', 'r') as f:
    data = [int(val) for val in f.readlines()]

calc_list = data

def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1

def best_profit(psdata):
    global min_value, max_value, best
    if len(psdata) <= 1:
        return 0
    left = psdata[:len(psdata)//2]
    right = psdata[len(psdata)//2:]

    left_best = best_profit(left)
    right_best = best_profit(right)

    total_best = max(right) - min(left)
    
    if best < max(left_best, right_best, total_best) :
        best = max(left_best, right_best, total_best)
        max_value = max(right)
        min_value = min(left)
    elif best == max(left_best, right_best, total_best):
        if max_value > max(right):
            max_value = max(right)
        if min_value < min(left):
            min_value = min(left)
    

    return best

def find_time(data):
    global min_value, max_value

    min_time = 0; max_time = len(data)-1
    if data.count(min_value) > 1 and data.count(max_value) > 1:
        while min_time < max_time :
            if data[min_time] != min_value or min_value in data[min_time + 1:max_time]:
                min_time += 1
            if data[max_time] != max_value or max_value in data[min_time:max_time]:
                max_time -= 1
            if not(min_value in data[min_time + 1:max_time] or max_value in data[min_time:max_time]):
                break
    elif data.count(min_value) > 1:
        max_time = data.index(max_value)
        for i in range(max_time, -1, -1):
            if min_value == data[i]:
                min_time = i
                break
    else :
        min_time = data.index(min_value)
        for i in range(min_time + 1, len(data)):
            if max_value == data[i]:
                max_time = i
                break

    return min_time, max_time

bf = best_profit(data)
min_time, max_time = find_time(data)
print(bf)
print('min_value =', min_value, 'max value =', max_value)
print(min_time, max_time)
with open('sampleData4/allin.out', 'w') as f:
    f.write(str(min_time)+' '+str(max_time))