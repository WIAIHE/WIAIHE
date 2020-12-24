'''
输入一个大于 2 的正整数 n，求斐波那契数列前 n 项数。斐波那契
数列指的是这样一个数列：0、1、1、2、3、5、8、13、21、34……
对应的递推定义为：F(0)=0，F(1)=1,F(n)=F(n - 1)+F(n - 2)（n≥ 2，n 为
正整数）
'''

a = input()
a = int(a)
n1 = 0
n2 = 1
numlist = []
for x in range(a):
 numlist.append(n1)
 n1,n2 = n2,n1+n2
ostr = ""
for i in numlist:
 ostr += str(i) + ", "
print(ostr[:-2])
