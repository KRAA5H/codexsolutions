import math  # for pi

print()  # copied from instructions
print("==================")
print("Area Calculator 📐")
print("==================")
print()
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")
print()

choice = int(input("Which shape: "))
print()

if choice == 1:
    base = float(input("Base: "))  # float since base could be 5.6
    height = float(input("Height: "))
    area = 0.5 * base * height
elif choice == 2:
    length = float(input("Length: "))
    width = float(input("Width: "))
    area = length * width
elif choice == 3:
    side = float(input("Side: "))
    area = side * side
elif choice == 4:
    radius = float(input("Radius: "))
    area = math.pi * radius * radius
else:
    print()
    print("Exiting")


print()
print(f"The area is {area}")
