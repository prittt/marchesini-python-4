# Versione proposta da ChatGPT per compattare il mio codice in vector.py
# L'implementazione di ChatGPT è stata leggermente ritoccata

from typing import Union, List, Tuple, Set, Self

Number = Union[int, float]

class Vector:
    def __init__(
        self,
        *args: Union[Number, List[Number], Tuple[Number, ...], Set[Number]]
    ):
        if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
            self.__data: List[Number] = list(args[0])
        else:
            self.__data: List[Number] = list(args)

    def __str__(self) -> str:
        return f"{self.__data}"

    def __repr__(self) -> str:
        return self.__str__()

    def _apply_operation(self, other: Union[Self, Number], op) -> Self:
        if isinstance(other, Vector):
            if len(self.__data) != len(other.__data):
                raise ValueError(
                    "I vettori devono avere la stessa lunghezza per l'operazione."
                )
            return Vector([op(a, b) for a, b in zip(self.__data, other.__data)])
        elif isinstance(other, (int, float)):
            return Vector([op(a, other) for a in self.__data])
        else:
            return NotImplemented

    def __add__(self, other: Union[Self, Number]) -> Self:
        return self._apply_operation(other, lambda a, b: a + b)

    def __radd__(self, other: Number) -> Self:
        return self.__add__(other)

    def __iadd__(self, other: Union[Self, Number]) -> Self:
        result = self.__add__(other)
        self.__data = result.__data
        return self

    def __neg__(self):
        return Vector([-x for x in self.__data])

    def __sub__(self, other: Union[Self, Number]) -> Self:
        return self._apply_operation(other, lambda a, b: a - b)

    def __rsub__(self, other: Number) -> Self:
        return (-self) + other

    def __isub__(self, other: Union[Self, Number]) -> Self:
        result = self.__sub__(other)
        self.__data = result.__data
        return self

v1 = Vector([1, 2, 3, 4, 5])
print(v1)
v2 = Vector((1, 2, 3, 4, 5))
print(v2)
v3 = Vector({1, 2, 3, 4, 5})
print(v3)
v4 = Vector(1, 2, 3, 4, 5)
print(v4)

v5 = v1 + v2
v1 = v1 + v2
v1 += v2
v1 = v1 + 4
v1 = 4 + v1
v1 += 4

v5 = v1 - v2
v1 -= v2
v1 = v1 - 4
v1 = 4 - v1
v1 -= 4
pass