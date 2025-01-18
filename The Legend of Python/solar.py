from math import pi
from random import choice as ch

planets = ["Mercury", "Venus", "Earth", "Mars", "Saturn"]

sphere_sa = lambda radius: 4 * pi * radius**2

random_planet = ch(planets)

if random_planet == "Mercury":
    r = 2440
elif random_planet == "Venus":
    r = 6052
elif random_planet == "Earth":
    r = 6371
elif random_planet == "Mars":
    r = 3390
elif random_planet == "Saturn":
    r = 58232
else:
    print("Not a planet")
    r = None

if r is not None:
    area = sphere_sa(r)
    print(
        f"The surface area of {random_planet} is {area:.2f} or {round(area)} square kilometers."
    )
