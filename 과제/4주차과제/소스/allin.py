data = list()
with open('allin.inp', 'r') as f:
    data = [int(x) for x in f.readlines()]
data = data[1:]

def bp(data):
    _buy = 0
    buy = 0
    sell = 0
    best = 0
    for time in range(1, len(data)):
        _best = data[time] - data[_buy]
        if _best > best:
            best = _best
            buy = _buy
            sell = time
        elif _best == best and _buy != buy and _buy > buy:
            buy = _buy
            sell = time
        elif _best <= 0:
            _buy = time

    return buy, sell

buy, sell = bp(data)

with open('allin.out', 'w') as f:
    f.write(str(buy + 1) + ' ' + str(sell + 1))