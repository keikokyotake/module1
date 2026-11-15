# Программа для расчета посещаемости учебной группы. Автор: Цой Кирилл.

# Ширина полей отчета и таблицы
WIDTH = 45

# Получает положительное целое число по запросу и возвращает его.
def getPositiveInteger(prompt):
    value = input(prompt)
    while not value.isdigit() or int(value) <= 0:
        print("Ошибка! Введите положительное целое число.")
        value = input(prompt)
    return int(value)

# Получает число присутствующих в пределах численности группы и возвращает его.
def getAttendance(total):
    present = int(input("Введите число присутствующих: "))
    while present < 0 or present > total:
        print("Ошибка! Число присутствующих должно быть от 0 до", total)
        present = int(input("Введите число присутствующих: "))
    return present

# Получает процент посещаемости и возвращает категорию посещаемости.
def getCategory(percent):
    if percent < 60:
        return "Низкая"
    elif percent < 85:
        return "Средняя"
    else:
        return "Высокая"

# Рассчитывает и выводит отчет и прогноз посещаемости для заданной группы.
def printReport(groupName, total, present):
    absent = total - present
    percent = present / total * 100
    category = getCategory(percent)
    
    print()
    print("-" * WIDTH)
    print(f"{'ОТЧЕТ О ПОСЕЩАЕМОСТИ':^{WIDTH}}")
    print("-" * WIDTH)
    print(f"{'Группа:':<30}{groupName:>{WIDTH - 30}}")
    print(f"{'Численность группы:':<30}{total:>{WIDTH - 30}d}")
    print(f"{'Присутствующие:':<30}{present:>{WIDTH - 30}d}")
    print(f"{'Отсутствующие:':<30}{absent:>{WIDTH - 30}d}")
    print(f"{'Посещаемость:':<30}{percent:>{WIDTH - 31}.1f}%")
    print(f"{'Категория:':<30}{category:>{WIDTH - 30}}")
    print("-" * WIDTH)

    print(f"{'ПРОГНОЗ ПОСЕЩАЕМОСТИ':^{WIDTH}}")
    print("-" * WIDTH)
    print(f"{'Увеличение':>10}{'Присутствующие':>20}{'Процент':>15}")
    print("-" * WIDTH)

    for increase in range(1, 6):
        newPresent = present + increase
        if newPresent > total:
            newPresent = total
        newPercent = newPresent / total * 100
        print(f"{increase:>10d}{newPresent:>20d}{newPercent:>14.1f}%")

    print("-" * WIDTH)

# Организует ввод данных, расчеты и повторение программы для другого занятия.
def main():
    repeat = "да"

    while repeat == "да":
        groupName = input("\nВведите название группы: ")
        total = getPositiveInteger("Введите общую численность группы: ")
        present = getAttendance(total)

        printReport(groupName, total, present)

        repeat = input(
            "\nРассчитать посещаемость другого занятия? (да/нет): "
        ).strip().lower()

        while repeat != "да" and repeat != "нет":
            print("\nПожалуйста, введите «да» или «нет».")
            repeat = input(
                "Рассчитать посещаемость другого занятия? (да/нет): "
            ).strip().lower()

    print("\nРабота программы завершена")

if __name__ == "__main__":
    main()
