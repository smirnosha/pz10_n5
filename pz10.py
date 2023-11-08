import pandas as pd
import re

# Задание 1. Разделить компоненты по 2м группам - Сборка и Компонент, ответ вписать в столбец H
df = pd.read_excel('Машина 1.xlsx')
df['Группа компонента'] = df.apply(
    lambda row: 'Сборка' if row['Наименование компоненты'] in ["Кузов", "Салон", "Подвеска", "Двигатель",
                                                               "Трансмиссия"] else 'Компонент', axis=1)

# Задание 2. Создать вручную 2 словаря Крепеж = {Болт, Гайка, Штифт, Шайба, Шуруп} Декор = {Коврики, Подушки}
krepezh = {'Болт', 'Гайка', 'Штифт', 'Шайба', 'Шуруп'}
dekor = {'Коврики', 'Подушки'}


# Задание 3. Присвоить каждой строке категорию - Крепеж, Декор, Сборка, Детали.
def category(row):
    if row['Наименование компоненты'] in krepezh:
        return 'Крепеж'
    elif row['Наименование компоненты'] in dekor:
        return 'Декор'
    elif 'Сборка' in row['Группа компонента']:
        return 'Сборка'
    else:
        return 'Детали'


df['Категория'] = df.apply(category, axis=1)


# Задание 4. Проанализировав код компоненты, разделить все компоненты на 3 группы по производителю - Иностранное, РФ по ГОСТ, РФ.
def isLatin(text):
    return bool(re.search('[^a-zA-Z а-яА-ЯёЁ]', text))


def components(component):
    if isLatin(component) or component.isnumeric():
        return 'Иностранное'
    elif 'ГОСТ' in component:
        return 'РФ по ГОСТ'
    elif any(char.isalpha() for char in component):
        return 'РФ'


df['Производитель'] = df['Код компоненты'].apply(components)

# Запись результата в excel файл 'Машина 1-разметка.xlsx'
df.to_excel('Машина 1-разметка.xlsx', index=False)
