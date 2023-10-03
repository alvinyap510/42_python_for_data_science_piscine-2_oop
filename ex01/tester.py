from S1E7 import Baratheon, Lannister

Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaine = Lannister.create_lannister("Jaine", True)
print(
    f"Name: {Jaine.first_name, type(Jaine).__name__}, Alive: {Jaine.is_alive}"
)

# __str__ -> return value was meant to use by str(object) or object.__str__()
# to create a string

# __repr__ -> return value should be an unambigous representation of the
# object, and can use eval() to recrate the object

# if __str__ and __repr__ not overridden
# print(Robert.__str__)
# -> <method-wrapper '__str__' of Baratheon object at 0x1048be560>
# print(str(Robert))
# -> <S1E7.Baratheon object at 0x1048be560>
# print(Robert.__repr__)
# -> <method-wrapper '__repr__' of Baratheon object at 0x1048be560>
# print(Robert.__repr__())
# -> <S1E7.Baratheon object at 0x1048be560>

# if __str__ not overriden but __repr__ overridden
# print(Robert.__str__)
# -> <method-wrapper '__str__' of Baratheon object at 0x1048be560>
# print(str(Robert))
# -> Vector: ('Baratheon', 'brown', 'dark')
# print(Robert.__repr__)
# -> <method-wrapper '__repr__' of Baratheon object at 0x1048be560>
# print(Robert.__repr__())
# -> Vector: ('Baratheon', 'brown', 'dark')

# if __str__ overriden but __repr__ not overridden
# print(Robert.__str__)
# -> <bound method Baratheon.__str__ of
# <S1E7.Baratheon object at 0x100362560>>
# print(str(Robert))
# -> Class of Baratheon, with brown eyes and dark hairs
# print(Robert.__repr__)
# -> <method-wrapper '__repr__' of Baratheon object at 0x100362560>
# print(Robert.__repr__())
# -> <S1E7.Baratheon object at 0x100362560>

# if __str__ and __repr__ both overridden
# print(Robert.__str__)
# -> <bound method Baratheon.__str__ of
# Vector: ('Baratheon', 'brown', 'dark')>
# print(str(Robert))
# -> Class of Baratheon, with brown eyes and dark hairs
# print(Robert.__repr__)
# -> <bound method Baratheon.__repr__ of
# Vector: ('Baratheon', 'brown', 'dark')>
# print(Robert.__repr__())
# -> Vector: ('Baratheon', 'brown', 'dark')
