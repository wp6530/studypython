#-*-coding=utf-8-*-
import time
# 001��Ŀ�����ĸ����֣�1��2��3��4������ɶ��ٸ�������ͬ�����ظ����ֵ���λ�������Ƕ��٣�
# print("++++++++++++++++++001++++++++++++++++++++++++")
# total=0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#                 if((i!=j)and(i!=k)and(j!=k)):
#                     print(i,j,k)
#                     total+=1
#
# print(total)
#
# print("++++++++++++++++++002++++++++++++++++++++++++")
# import itertools
#
# sum2 = 0
# a = [1, 2, 3, 4]
# for i in itertools.permutations(a, 3):
#     print(i)
#     sum2 += 1
# print(sum2)

# 002 ��˰����
# profit = int(input('Show me the money: '))
# bouns = 0
# rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
# thresholds = [100000, 100000, 200000, 200000, 400000]
#
# for i in range(len(thresholds)):
#     # print("thresholds[i]:", thresholds[i])
#     if profit <= thresholds[i]:
#         bouns += profit*rates[i]
#         profit = 0
#         break
#     else:
#         bouns += thresholds[i]*rates[i]
#         profit -=thresholds[i]
# bouns += profit*rates[-1]
# print(bouns)

# 003 ��ȫƽ����
# 004 ����ڼ���
# 005 ��������
# raw = []
# for i in range(3):
#     x = int(input('int%d: '%(i)))
#     raw.append(x)
# print(sorted(raw))

# 009 ��ͣ1�����
# for i in range(4):
#     print(str(int(time.time()))[-2:])
#     time.sleep(1)


## 010 ��ʽ��ʱ��
for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)




















