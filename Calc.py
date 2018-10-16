'''
Created on Oct 12, 2018

@author: Matt Discepola
'''


name = input("Please input your name: ")

print("Hello, ", name, ", welcome to the algebra and geometry calculator.", sep="")
print("Press Enter to Continue")
input("")
print("Area of a Triangle")
triBase =  float(input("Please input the value of the  base: "))
triHeight = float(input("Please input the value of the height: "))
triUnit = input("Please input the unit of measurement: ")
triArea = triBase * triHeight / 2
print("The area of that triangle is ", format(triArea, '.2f'), " ", triUnit, "²", sep="")
print("Press enter to continue")
input("")
print("Volume of a Cube")
cubeSide = float(input("Please input the value of a side: "))
cubeUnit = input("Please input the unit of measurement: ")
cubeVolume = cubeSide * cubeSide * cubeSide
print("The volume of that cube is ", format(cubeVolume, '.2f'), " ", cubeUnit, "³", sep="")
print("Goodbye, ", name, ", thank you for using this calculator.", sep="")