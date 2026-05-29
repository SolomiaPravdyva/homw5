class CustomList:
    def __init__(self, data=None):
        self._data = []
        if data == None:
            return
        if isinstance(data, CustomList):
            data = data._data
        for x in data:
            if type(x) != int:
                raise TypeError("CustomList може містити лише цілі числа")
            self._data.append(x)
    def __str__(self):
        return f"CustomList({self._data}), size={len(self._data)}"
    def __len__(self):
        return len(self._data)
    def __getitem__(self, index):
        return self._data[index]
    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError("Тільки int")
        self._data[index] = value
    def __contains__(self, item):
        return item in self._data
    def __iadd__(self, other):
        if isinstance(other, CustomList):
            self._data.extend(other._data)
        elif isinstance(other, int):
            self._data.append(other)
        else:
            return NotImplemented
        return self
    def __isub__(self, other):
        if isinstance(other, CustomList):
            for x in other._data:
                while x in self._data:
                    self._data.remove(x)
        elif isinstance(other, int):
            while other in self._data:
                self._data.remove(other)
        else:
            return NotImplemented
        return self
    def __imul__(self, n):
        if not isinstance(n, int):
            raise TypeError("Потрібне ціле число")
        self._data *= n
        return self
cl = CustomList()
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        for part in line.split():
            if part.lstrip("-").isdigit():
                cl += int(part)

total_sum = sum(cl._data)
count = len(cl)
special = {1, 3, 1984, 7777}
has_special = False
for x in special:
    if x in cl:
        has_special = True
        break

non_zero_count = sum(1 for x in cl if x != 0)

print("Список:", cl)
print("Сума:", total_sum)
print("Кількість чисел:", count)
print("Є 1, 3, 1984, 7777?:", has_special)
print("Ненульових чисел:", non_zero_count)
