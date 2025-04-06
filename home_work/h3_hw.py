def compare (a, b):
    if a > b:
        print (a)
    elif b >a:
        print (b)
    else:
        print('числа равны')
compare(10, 56)

def yes_no (a, b):
    if abs(a-b)==135:
        print('yes')
    else:
        print ('no')
yes_no(570, 435)


def season (b):
    if b == 12 or b== 1 or b== 2:
        print('зима')
    elif b in range (3, 6):
        print('весна')
    elif b in range (6, 9):
        print('лето')
    elif b in range (9, 12):
        print('осень')
    else:
        print('такого месяца нет')
season(11)


def ten (a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('yes')
    else:
        print ('no')
ten (25, 15, 46)


def five_List (a: list):
    if len(a)>5:
        print('введено больше 5 значений')
    else:
        kol=[num for num in a if num>0]
        print(len(kol))
five_List([0, 2, -3, 4, 5])


def days_in_year (y: int, m: int):
    if y == 0 and m in range (1, 13):
        days=m*29
        print (days)
    elif y >=0 and m==0:
        days=y*12*29
        print (days)
    elif y>0 and m in range (1, 13):
        days=y*m*29
        print (days)
    else:
        print ('ошибка')
days_in_year(12, 13)

