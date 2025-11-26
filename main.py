# Класс с реализацией пузырьковой сортировки
class Sorter:
    @staticmethod
    def sort(data: list) -> list:
        try:
            # Проверяем, что входной аргумент - список
            if not isinstance(data, list):
                print("Ожидался список (list).")
                return []

            # Внешний цикл пузырьковой сортировки
            for i in range(len(data) - 1):
                swapped = False
                # Внутренний цикл - попарное сравнение соседних элементов
                for j in range(len(data) - i - 1):
                    # Меняем элементы местами, если стоят в неверном порядке
                    if data[j] > data[j + 1]:
                        data[j], data[j + 1] = data[j + 1], data[j]
                        swapped = True
                # Если за проход не было ни одной перестановки - массив уже отсортирован
                if not swapped:
                    break

            return data

        # Ошибка: элементы внутри списка нельзя сравнить
        except TypeError:
            print("Элементы списка должны быть сравнимыми.")
            return []
        # Общая обработка неожиданных ошибок
        except Exception as err:
            print(f"Ошибка при сортировке: {err}")
            return []


# Пример использования
if __name__ == "__main__":
    a = [2, 1, 9, -4, 0]
    s = Sorter()
    print(s.sort(a))
