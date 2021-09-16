# ---------------------------------------------------------------------
# Filename      : class-vars.py
# Location      : ./Session-09
# Project       : Class-Examples
# Author        : Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created       : 16/9/21
# Version       : 0.1
# Description   :
#   This is a description of what the file is for
#
# ---------------------------------------------------------------------

class Car:
    wheels = 4    # <- Class variable
    def __init__(self, name):
        self.name = name    # <- Instance variable

    @staticmethod
    def add_wheel():
        Car.wheels += 1


jag = Car('jaguar')
fer = Car('ferrari')

print(jag.name, fer.name)
print(jag.wheels, fer.wheels, Car.wheels)

Car.wheels = 3
print(jag.name, fer.name)
print(jag.wheels, fer.wheels, Car.wheels)
fer.wheels = 5
print(jag.name, fer.name)
print(jag.wheels, fer.wheels, Car.wheels)
Car.add_wheel()
print(jag.name, fer.name)
print(jag.wheels, fer.wheels, Car.wheels)
print(fer.wheels, fer.__class__.wheels)

