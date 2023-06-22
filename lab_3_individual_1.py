"""
3. Дано число ( ). Вывести на экран название дня недели, который соответствует
этому номеру.
"""

def get_user_numbers(m):
    if m >= 1 and m <=7:
        if m == 1: print("Понедельник")
        elif m == 2: print("Вторник")
        elif m == 3: print("Среда")
        elif m == 4: print("Четверг")
        elif m == 5: print("Пятница")
        elif m == 6: print("Суббота")
        elif m == 7: print("Воскресенье")
    else:
        get_user_numbers(int(input("Введите число от 1 до 7: ")))

if __name__ == "__main__":
    get_user_numbers(int(input("Введите число от 1 до 7: ")))
