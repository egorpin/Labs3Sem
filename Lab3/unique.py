from .gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)

        self.unique_items = set()

    def __next__(self):
        while True:
            item = next(self.items)
            item = item.lower() if self.ignore_case else item

            if item not in self.unique_items:
                self.unique_items.add(item)
                return item

    def __iter__(self):
        return self

if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    unique_data = Unique(data)
    print(list(unique_data))

    data = gen_random(10, 1, 3)
    unique_data = Unique(data)
    print(list(unique_data))

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique_data = Unique(data)
    print(list(unique_data))

    unique_data_ignore_case = Unique(data, ignore_case=True)
    print(list(unique_data_ignore_case))
