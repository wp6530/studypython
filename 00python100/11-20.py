# -*-coding=utf-8-*-
# 011��������
# ��һ�����ӣ��ӳ������3������ÿ���¶���һ�����ӣ�
# С���ӳ����������º�ÿ��������һ�����ӣ�
# �������Ӷ���������ÿ���µ���������Ϊ���٣�
mature = 1
one_mouth = 0
two_mouth = 0
three_mouth = 0
mouths = 9
for i in range(mouths):
    one_mouth, two_mouth, three_mouth, mature = mature, one_mouth,two_mouth,three_mouth+mature
print("one_mouth:", one_mouth)
print("two_mouth:", two_mouth)
print("three_mouth:", three_mouth)
print("mature:", mature)
print("all:", one_mouth+two_mouth+three_mouth+mature)
