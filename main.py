class Sorter:
    def sort(self, data: list) -> list:
        ...


if __name__ == "__main__":
    a = [2, 1, 9, -4, 0]
    s = Sorter()
    print(s.sort(a))
