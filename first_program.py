a= input()
b = input()
if a=="красный":
    if b=="синий":
        print("фиолетовый")
    elif b=="желтый":
        print("оранжевый")
    elif a==b:
        print("красный")
    else:
        print("ошибка цвета")
elif a=="синий":
    if b=="красный":
        print("фиолетовый")
    elif b=="желтый":
        print("зеленый")
    elif a==b:
        print("синий")
    else:
        print("ошибка цвета")

elif a=="желтый":
    if b=="красный":
        print("оранжевый")
    elif b=="синий":
        print("зеленый")
    elif a==b:
        print("желтый")
    else:
        print("ошибка цвета")
else:
    print("ошибка цвета")