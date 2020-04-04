data = list()
with open('sampleData4/3.inp', 'r') as f:
    data = [int(x) for x in f.readlines()]
print('data = ', data)
data = data[1:]

def bp(data):
    if len(data) <= 1:
        return 0

    right = data[len(data)//2:]
    left = data[:len(data)//2]

    right_best = bp(right)
    left_best = bp(left)

    total_best = max(right) - min(left)

    return max(total_best, right_best, left_best)
    
def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1    

def best_profit(data):
    best = 0
    min_time = 0
    max_time = len(data)
    for i in range(0, len(data) - 1):
        min_value = min(data[:i+1])
        max_value = max(data[i+1:])
    
        if best < max_value - min_value:
            best = max_value - min_value
            min_time = listRightIndex(data[:i+1], min_value)
            max_time = i + data[i+1:].index(max_value) + 1
        elif best == max_value - min_value:
            min_time = listRightIndex(data[:i+1], min_value)
            max_time = i + data[i+1:].index(max_value) + 1
    print(best)
    return min_time, max_time



min_time, max_time = best_profit(data)
# buy, sell = _bp(data)
best = bp(data)
print('best = ', best)
print(min_time, max_time)
# print(buy, sell)
with open('sampleData4/3.out', 'r') as f:
    print('정답은 = ', f.readline())

with open('sampleData4/allin.out', 'w') as f:
    f.write(str(min_time) + ' ' + str(max_time))
