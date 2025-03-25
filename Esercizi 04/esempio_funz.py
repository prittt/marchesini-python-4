# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     @property
#     def age(self):
#         return self.__age - 2

#     @age.setter
#     def age(self, new_age):
        
#         if new_age < 30:
#             self.__age = new_age
#         else:
#             print("Never! I am always under 30!")

# person = Person("Josiah Wang", 20)
# print(type(Person.age))
# print(Person.age())
# print(dir(Person.age))
# print(person.age)
# person.age = 10
# print(person.age)
# person.age = 70
# print(person.age)
# print(person.__age) ## this won't work!

# class Contatore:
#     def __init__(self):
#         self.chiamate = 0

#     def __call__(self, funzione):
#         def wrapper(*args, **kwargs):
#             self.chiamate += 1
#             print(f"Chiamata numero {self.chiamate}")
#             return funzione(*args, **kwargs)
#         return wrapper

# @Contatore()
# def saluta():
#     print("Ciao!")

# print(type(saluta))
# saluta()
# saluta()
# saluta()
# saluta()

# #####################################################

# def log_istanziazione(cls):
#     class NuovaClasse(cls):
#         def __init__(self, *args, **kwargs):
#             print(f"Creazione di un'istanza di {cls.__name__}")
#             super().__init__(*args, **kwargs)
#     return NuovaClasse

# @log_istanziazione
# class Prova:
#     def __init__(self, valore):
#         self.valore = valore

# # Creiamo un'istanza per vedere l'effetto
# print(Prova)
# p = Prova(10)

#####################################################

def aggiungi_metodo(cls):
    def nuovo_metodo(self):
        return "Nuovo metodo aggiunto!"
    
    cls.nuovo_metodo = nuovo_metodo
    return cls

@aggiungi_metodo
class MiaClasse:
    def esistente(self):
        return "Metodo originale"


# Uso della classe decorata
oggetto = MiaClasse()
print(oggetto.esistente())      # Output: Metodo originale
print(oggetto.nuovo_metodo())   # Output: Nuovo metodo aggiunto!

#####################################################

def con_tag(tag):
    def decoratore(cls):
        cls.tag = tag  # Aggiunge un attributo alla classe
        return cls
    return decoratore

@con_tag("Importante")
class Documento:
    pass

print(Documento)
print(type(Documento))
print(Documento.tag)  # Output: Importante

#####################################################
