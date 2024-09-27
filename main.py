def calculate_control_digit(pinfl):
    """Вычисление контрольной цифры ПИНФЛ"""
    weights = [7, 3, 1]  # Весовые коэффициенты
    total_sum = 0

    for i, digit in enumerate(pinfl[:17]):  # Первые 17 цифр ПИНФЛ
        weight = weights[i % 3]  # Циклически повторяем веса 7, 3, 1
        total_sum += int(digit) * weight

    control_digit = total_sum % 10  # Контрольная цифра - остаток от деления на 10
    return control_digit


def generate_pinfl(gender_century_index, birth_date, region_code, serial_number):
    """
    Генерация ПИНФЛ.

    :param gender_century_index: Индекс пола и века рождения (1-6)
    :param birth_date: Дата рождения в формате ДДММГГ
    :param region_code: Код региона
    :param serial_number: Порядковый номер (4 цифры)
    :return: ПИНФЛ с контрольной цифрой
    """
    # Формирование первых 17 цифр ПИНФЛ
    pinfl = f"{gender_century_index}{birth_date}{region_code}{serial_number}"

    # Вычисление контрольной цифры
    control_digit = calculate_control_digit(pinfl)

    # Полный ПИНФЛ
    pinfl += str(control_digit)

    return pinfl


# Получение данных от пользователя через терминал
gender_century_index = input("Введите индекс пола и века рождения (1-6): ")
birth_date = input("Введите дату рождения в формате ДДММГГ: ")
region_code = input("Введите код региона: ")
serial_number = input("Введите порядковый номер (4 цифры): ")

# Генерация ПИНФЛ
pinfl = generate_pinfl(gender_century_index, birth_date, region_code, serial_number)
print("Сгенерированный ПИНФЛ:", pinfl)