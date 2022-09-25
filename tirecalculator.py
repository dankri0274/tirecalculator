import math

inch = 2.54

def calculate(width, perc, inches, mode):
	width = int(width)
	perc = int(perc)
	inches = int(inches)
	mode = int(mode)

	tireHeight = width * perc / 100
	diameter = (inches * inch) * 10 + tireHeight
	circ = round(diameter * math.pi / 10, 2)

	if mode == 1: # Circumference
		return circ
	if mode == 2: # Rotations per second
		return round((kmh / 3.6 / circ / 10) * 1000, 2)

dimensions = input("Enter your tire dimension like this (205/55 R 16): ")
d = dimensions.split(' ')
d2 = d[0].split('/')

kmh = int(input("Enter speed (km/h): "))

print(f"\nDimensions: {d2[0]}/{d2[1]} R{d[2]}")
print(f"The circumference of your tire is {calculate(d2[0], d2[1], d[2], 1)}cm")
print(f"At {kmh} km/h the tire does {calculate(d2[0], d2[1], d[2], 2)} rot/s\n")