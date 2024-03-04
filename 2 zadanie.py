a = int(input("введите своё место: "))
if a <= 0 or a >= 55:
    print("ошибка")
else:
    if a % 2 == 0:
        s = "верхнее"
    else:
        s = "нижнее"
    if a in range(37, 55):
        b = "боковое"
    else:
        b = "обычное"
    print(s, b)
