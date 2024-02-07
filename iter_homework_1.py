import time


class FlatIterator:

    def __init__(self, list_of_list):
        self.counter = 0
        self.res = []
        self.flatten_list = self.getVal(list_of_list)

    def getVal(self, nl):
        result_list = []
        for item in nl:
            if item is None:
                self.res.append(None)
                continue

            if isinstance(item, (int, bool, str)):
                self.res.append(item)
            else:
                self.getVal(item)
        return result_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.res):
            raise StopIteration

        else:
            result = self.counter
            self.counter += 1
            return self.res[result]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

