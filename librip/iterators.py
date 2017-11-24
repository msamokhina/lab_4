# Итератор для удаления дубликатов
class Unique(object):
    # будем хранить в этой переменной
    # все полученные объекты items
    _lst = []

    def __init__(self, items, ignore_case):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        assert len(items) > 0
        self._lst = list(items)
        self.ignore_case = ignore_case
        self.returned = list()


    def __next__(self):
        for x in self._lst:
            if (self.ignore_case & isinstance(x, str)):
                if x.lower() not in self.returned:
                    self.returned.append(x.lower())
                    return x
            else:
                if x not in self.returned:
                    self.returned.append(x)
                    return x
        raise StopIteration()

    def __iter__(self):
        return self
