age_dog = int(input())

if age_dog <= 2:
    print(10.5 * age_dog)
elif age_dog > 2:
    print((2 * 10.5) + ((age_dog -2) * 4))
else:
    print("Ошибка")