"""
16. Ученик выучил в первый день 5 английских слов. В каждый следующий день он выучивал на
2 слова больше, чем в предыдущий. Сколько английских слов выучит ученик в 10-ый день
занятий
"""

if __name__ == "__main__":
    student = 5
    n = 0
    for i in range(1, 10):
         n += 2
         print(student + n)