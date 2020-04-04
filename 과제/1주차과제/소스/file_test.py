# with open('./text_test/text.txt', 'r') as f:
#     c = f.read()
#     print(c)
#     print(list(c))

#  한문장씩 읽어오기
with open('./text_test/text.txt', 'r') as f:
    for c in f:
        print(c)

score = list()
with open('./text_test/integer.txt', 'r') as n:
    for line in n:
        score.append(int(line))
    print(score)

print(max(score))

# 파일 쓰기
with open('./text_test/write.txt', 'w') as f:
    f.write('This is test message for write.\n')