# Итератор для удаления дубликатов
class Unique(object):
    # будем хранить в этой переменной
    # все полученные объекты items
    _lst = []
    # будем хранить уникальные объекты
    # в этой переменной
    _new_lst = []
    _index = -1

    def __init__(self, items, ignore_case):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        assert len(items) > 0
        self._lst = list(items)

        if ignore_case & isinstance(self._lst[0], str):
            self._lst.sort(key = lambda char: char.lower())
        else:
            self._lst.sort()

        self._new_lst = []
        current_index = 0
        self._new_lst.append(self._lst[0])

        for x in self._lst:
            if(ignore_case & isinstance(self._lst[0], str)):
                if(x.lower() != self._new_lst[current_index].lower()):
                    self._new_lst.append(x)
                    current_index += 1
            else:
                if(x != self._new_lst[current_index]):
                    self._new_lst.append(x)
                    current_index += 1

    def __next__(self):
        if self._index >= len(self._new_lst) - 1:
            raise StopIteration
        self._index += 1
        return self._new_lst[self._index];

    def __iter__(self):
        return self