import math

class Rational:
    def __init__(self, n, d=1):
        if d == 0:
            raise ValueError("Знаменник != нулю.")
        common = math.gcd(n, d)
        self._n=n//common
        self._d=d//common
        if self._d<0:
            self._n*=-1
            self._d*=-1
    @property
    def n(self):
        return self._n
    @property
    def d(self):
        return self._d
    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)
    def __radd__(self, other):
        return self.__add__(other)
    def __repr__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else f"{self.n}"

class RationalList:
    def __init__(self, elements=None):
        self._data = []
        if elements:
            for item in elements:
                self.append(item)
    def append(self, item):
        if not isinstance(item, Rational):
            raise TypeError("Елементом RationalList може бути лише об'єкт класу Rational")
        self._data.append(item)
    def __getitem__(self, index):
        return self._data[index]
    def __setitem__(self, index, value):
        if not isinstance(value, Rational):
            raise TypeError("Значення має бути об'єктом Rational")
        self._data[index] = value
    def __len__(self):
        return len(self._data)
    def __add__(self, other):
        new_list = RationalList(self._data)
        if isinstance(other, RationalList):
            new_list._data.extend(other._data)
        elif isinstance(other, (Rational, int)):
            item = other if isinstance(other, Rational) else Rational(other)
            new_list.append(item)
        else:
            return NotImplemented
        return new_list
    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self._data.extend(other._data)
        elif isinstance(other, (Rational, int)):
            item = other if isinstance(other, Rational) else Rational(other)
            self.append(item)
        else:
            return NotImplemented
        return self
    def sum_all(self):
        res = Rational(0)
        for item in self._data:
            res += item
        return res
def process_file(filename):
    rl = RationalList()
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.split()
                for p in parts:
                    if '/' in p:
                        n, d = map(int, p.split('/'))
                        rl += Rational(n, d)
                    else:
                        rl += Rational(int(p))
        print(f"Файл {filename}: Сума = {rl.sum_all()}")
        return rl
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None
process_file("input01.txt")
#process_file("input02.txt")
#process_file("input03.txt")
