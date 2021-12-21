from rectangle import Rectangle
from triangle import Triangle

rec = Rectangle()
tri = Triangle()

rec.set_values(50,40)
tri.set_values(50,40)

rec.set_color('Blue')
tri.set_color('Red')

print(rec.area())
print(tri.area())

print(rec.get_color())
print(tri.get_color())