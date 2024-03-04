import random
print("1-красный, 2-синий, 3-жёлтый")
a = random.randint(1, 6)
b = random.randint(1, 6)
if a in range(1, 3) and b in range(2, 4):
    if a == 1 and b == 2:
        print("к+с=фиолетовый")
    if a == 2 and b == 1:
        print("с+к=фиолетовый")
    if a == 2 and b == 3:
        print("с+ж=зелёный")
    if a == 3 and b == 2:
        print("ж+с=зелёный")
    if a == 1 and b == 3:
        print("к+ж=оранжевый")
    if a == 3 and b == 1:
        print("ж+к=оранжевый")
else:
    print("ошибка")