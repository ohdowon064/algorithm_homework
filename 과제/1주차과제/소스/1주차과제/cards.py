"""
    카드게임
    연속된 숫자 중에서 빠진 2개의 숫자를 찾아라.
    입력
    첫줄. 숫자개수
    그다음 순서없는 숫자들

    출력
    빠진 2개의 숫자를 오름차순으로 출력

    조건. 배열계열의 자료구조 금지

    방법
    1부터 N까지의 합을 구하고 해당 입력된 숫자들을 뺀다.
    합과 곱이 이용
"""
end = 0
original_sum = 0
original_mul = 1

total_sum = 0
total_mul = 1

missing = 0
with open('./cards.inp', 'r') as f:
    end = int(f.readline())
    print(end)
    for i in range(1, end + 1):
        original_sum += i
        original_mul *= i

    for num in f:
        total_sum += int(num)
        total_mul *= int(num)

sum = original_sum - total_sum
mul = original_mul / total_mul

def calc(sum, mul) :
    x = int((sum - (sum**2 - 4 * mul)**0.5) / 2)
    y = int((sum + (sum**2 - 4 * mul)**0.5) / 2)
    return x, y
     
missing_num1, missing_num2 = calc(sum, mul)
with open('./cards.out', 'w') as f:
    f.write(str(missing_num1))
    f.write('\n')
    f.write(str(missing_num2))

print(missing_num1, missing_num2)
