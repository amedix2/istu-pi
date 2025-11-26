class Sorter:
    def sort(self, data: list) -> list:
        for i in range(len(data)):
            for j in range(len(data) - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


if __name__ == "__main__":
    a = [2, 1, 9, -4, 0]
    s = Sorter()
    print(s.sort(a))
