"""
We call a 'mutable' object in Python if it's value can be changed.
Built-in mutable objects in Python:
	- list
	- dict
	- set
	- Bytearray
"""

shopping_list = ["miilk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

a = b = c = d = e = f = another_list
print(a)
print("Adding cream")
b.append("cream")
print(c)
print(d)