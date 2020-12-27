m = int(input())
n = int(input())
for abc in range(m, n + 1):
    a = abc // 100
    bc = abc % 100
    b = bc // 10
    c = bc % 10
    if a**3 + b**3 + c**3 == abc:
        print(abc)