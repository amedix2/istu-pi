class Sorter:
    @staticmethod
    def sort(data: list) -> list:
        try:
            if not isinstance(data, list):
                print("Ожидался список (list).")
                return []

            for i in range(len(data) - 1):
                swapped = False
                for j in range(len(data) - i - 1):
                    if data[j] > data[j + 1]:
                        data[j], data[j + 1] = data[j + 1], data[j]
                        swapped = True
                if not swapped:
                    break

            return data

        except TypeError:
            print("Элементы списка должны быть сравнимыми.")
            return []
        except Exception as err:
            print(f"Ошибка при сортировке: {err}")
            return []


if __name__ == "__main__":
    a = [2, 1, 9, -4, 0]
    s = Sorter()
    print(s.sort(a))
