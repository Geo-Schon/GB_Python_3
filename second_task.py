"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не
должно быть дубликатов.
"""

draft_list = list(map(int, input('Введите числа списка через пробел: ').split()))
clean_list = list(set(draft_list))
print(f"Исходный список: {draft_list}")
print(f"Список без дубликатов: {clean_list}")