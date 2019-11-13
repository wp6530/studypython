# -*-coding=utf-8-*-
# 011：养兔子
# 有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
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
