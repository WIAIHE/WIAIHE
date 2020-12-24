'''
判断用户输入的非负整数是几位数，并给出其奇偶性，当输入为 0
时退出。
'''
while True:
     a = int(input())

    if a == 0:
        break

    print(len(str(a)))
    if a % 2 == 0:
        print('偶数')
    else:
        print('奇数')