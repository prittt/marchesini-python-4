class ZipIterator:
    def __init__(self, *iterables):
        self.iterators = [iter(it) for it in iterables]

    def __iter__(self):
        return self

    def __next__(self):
        # return tuple(next(it) for it in self.iterators)    
        items = []
        for it in self.iterators:
            try:
                items.append(next(it))
            except StopIteration:
                # Come zip: si ferma appena un iteratore finisce
                raise StopIteration
        return tuple(items)

for item in ZipIterator([1, 2, 3, 4], {'a', 'b', 'c'}, (True, False, True)):
    print(item)

from itertools import zip_longest

a = [1, 2, 3]
b = ['a', 'b']
c = [True]

for item in zip_longest(a, b, c):
    print(item)