'''
求三位数 M 和 N 之间所有三位水仙花数（包括 M 和 N），其个
位、十位、百位数字的立方和等于该数本身，例如：
153 = 1×1×1 + 5×5×5+ 3×3×3
'''
m = int(input())
n = int(input())
for abc in range(m, n + 1):
    a = abc // 100
    bc = abc % 100
    b = bc // 10
    c = bc % 10
    if a**3 + b**3 + c**3 == abc:
        print(abc)