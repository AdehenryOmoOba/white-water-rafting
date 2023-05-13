import math

# Area of a square = l^2
# Area of a circle = πr^2
# Area of a cylinder = 2πrh + 2πr^2

print()
print("Welcome, let's calculate the area of some shapes 😃")
print()

line = "--------------------------------------------------------------------------"

print(line)
square_length = input("What is the length (in centimeters) of a side of a square? ")
area_of_square = float(square_length) * float(square_length) 
print(f"The area of the square is: {area_of_square} square centimeters or {round(area_of_square / 10000, 4)} square meters")
print(f"The volume of a cube with side of length {square_length} centimeters is:", round(float(square_length) * float(square_length) * float(square_length), 2), "cubic centimeters")

print(line)

circle_radius = input("What is the radius (in centimeters) of a circle? ")
area_of_circle = 3.14 * float(circle_radius) * float(circle_radius) 
print("The area of the circle is:", round(area_of_circle, 2), "square centimeters or", round(area_of_circle / 10000, 4), "square meters")
sphere_volume = (4/3) * math.pi * float(circle_radius)**3
print(f"The volume of a sphere with radius {circle_radius} centimeters is:", round(sphere_volume, 2), "cubic centimeters")

print(line)

cylinder_radius = input("What is the radius (in centimeters) of a cylinder? ")
cylinder_height = input("What is the height (in centimeters) of the cylinder? ")
area_of_cylinder = (2 * (math.pi * float(cylinder_radius) * float(cylinder_height))) + (2 * (math.pi * float(cylinder_radius) * float(cylinder_radius)))
print("The area of the cylinder is:", round(area_of_cylinder, 2), "squre centimeters or", round(area_of_cylinder / 10000, 4), "square meters")
print(line)

print()

