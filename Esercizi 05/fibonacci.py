class FibonacciGenerator():
    def __init__(self, end = None):
        self.__a = -1
        self.__b = 1
        self.__end = end
        self.__index = 0
 
    def __iter__(self):
        return self

    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        self.__index += 1
        if self.__end and self.__index >= self.__end:
            raise StopIteration

        return self.__b


# for _, f in zip(range(10), FibonacciGenerator()):
#     print(f)


# -1  a
# 1   b a
# 0   b a   
# 1   a
# 1   
# 2   
# 3
# 5


def fibonacci_generator(end = 10):
    a, b = -1, 1
    index = 0
    while index < end:
        a, b = b, a + b
        yield b
        pass
a = fibonacci_generator(10)

for f in a: 
    print(f)
print(type(a))
for _, f in zip(range(10), fibonacci_generator()):
    print(f)

# for f in fibonacci_generator():
#     print(f)