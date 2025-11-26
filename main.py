class Sorter:
    @staticmethod
    def sort(data: list) -> list:
        for i in range(len(data) - 1):
            swapped = False
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
            if not swapped:
                break
        return data


if __name__ == "__main__":
    a = [2, 1, 9, -4, 0]
    s = Sorter()
    print(s.sort(a))
