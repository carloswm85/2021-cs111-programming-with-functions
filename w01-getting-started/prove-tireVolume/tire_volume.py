import math

""" Problem Statement: The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula: """

tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

value = math.pi * tire_width**2 * tire_aspect_ratio * (tire_width * tire_aspect_ratio + 2540 * tire_diameter)
ten_mill = 10000000
volume =round(value / ten_mill, 1)

print(f"The approximate volume is {volume} cubic cm.")