from typing import Union, List, Tuple, Set, Self
# from typing_extensions import Self

class Vector:
    def __init__(self, *args : Union[int, float, List[Union[int, float]], Tuple[Union[int, float]], Set[Union[int, float]]]):
        if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
            self.__data = list(args[0])
        else:
            self.__data = list(args)

    def __len__(self) -> int:
        return len(self.__data)

    def __str__(self):
        return f"{self.__data}"

    ######## ADD ########

    def __add__(self, other: Union[Self, int, float]) -> Self:  
        if isinstance(other, Vector):
            if len(self.__data) != len(other.__data):
                raise ValueError("Vectors must have the same length for addition")
            return Vector([a + b for a, b in zip(self.__data, other.__data)])
        elif isinstance(other, (int, float)):
            return Vector([a + other for a in self.__data])
    
        return NotImplemented

    def __iadd__(self, other: Self) -> Self:
        result = self + other
        self.__data = result.__data
        return self

    def __radd__(self, other: Union[int, float]) -> Self:
        return self + other
    
    ######## SUB ########    

    def __sub__(self, other: Union[Self, Union[int, float]]) -> Self:
        if isinstance(other, Vector):
            if len(self.__data) != len(other.__data):
                raise ValueError("Vectors must have the same length for subtraction")
            return Vector([a - b for a, b in zip(self.__data, other.__data)])
        elif isinstance(other, (int, float)):
            return Vector([a - other for a in self.__data])
        
        return NotImplemented

    def __neg__(self):
        return Vector([-x for x in self.__data])

    def __rsub__(self, other: Union[int, float]) -> Self:
        return -self + other

    def __isub__(self, other: Union[Self, Union[int, float]]) -> Self:
        result = self - other
        self.__data = result.__data
        return self
    
    def __getitem__(self, key: int | slice) -> Union[int, float] | Self:
        
        # if len(key) == 1:
        #     return self.__data[*key]
        # elif len(key) > 1:
        #     return Vector(self.__data[*key])
        
        # if isinstance(key, int):
        #     return self.__data[key] 
        # elif isinstance(key, slice):
        #     return Vector(self.__data[key])
        # return NotImplemented

        result = self.__data[key]
        return Vector(result) if isinstance(key, slice) else result

    def __setitem__(self, key: int | slice, value: Union[int, float] | List[Union[int, float]]) -> None:
        self.__data[key] = value


if __name__ == '__main__':
    v1 = Vector([1, 2, 3, 4, 5])
    print(v1)
    v2 = Vector((1, 2, 3, 4, 5))
    print(v2)
    v3 = Vector({1, 2, 3, 4, 5})
    print(v3)
    v4 = Vector(1, 2, 3, 4, 5)
    print(v4)

    print(v1[0])
    print(v1[0:3])
    v1[0] = 5
    v1[0:3] = [10, 11, 12]

    for v in v1:
        print(v)

    # v5 = v1 + v2
    # v1 = v1 + v2
    # v1 += v2
    # v1 = v1 + 4
    # v1 = 4 + v1
    # v1 += 4

    v5 = v1 - v2
    v1 -= v2
    print(v1 - 4)
    print(4 - v1)
    v1 -= 4
    pass