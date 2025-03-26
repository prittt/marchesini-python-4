class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc if doc is not None else fget.__doc__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("Attribute is not readable")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("Attribute is not writable")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("Attribute is not deletable")
        self.fdel(instance)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


# class MyClass:
#     def __init__(self):
#         self.__x = 0

#     def get_x(self):
#         return self.__x

#     def set_x(self, value):
#         print("Setting x to", value)
#         self.__x = value

#     def del_x(self):
#         print("Deleting x")
#         del self.__x

#     x = Property(get_x, set_x, del_x)


class MyClass:
    def __init__(self):
        self.__x = 0

    @Property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        del self.__x

obj = MyClass()

# 1. Accesso normale alla property
print(obj.x)

# 2. Modifica tramite property
obj.x = 50
print(obj.x)

# 3. Proviamo a "bypassare" la property
obj.__dict__['x'] = 999
print(obj.__dict__)         # x è nello __dict__, ma...

# 4. Vediamo se x nel __dict__ viene usato
print(obj.x)                # Continua a usare la property!
