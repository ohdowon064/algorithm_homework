a = [11, 22, 33, 44, 55]
print(a[::-1])

for i, v in enumerate(a):
    print(i)

print()
for i in a[::-1]:
        print(a.index(i))

print()
for i in range(len(a)-1, -1, -1):
    print(i)