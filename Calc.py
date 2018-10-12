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
print("The area of that triangle is", format(triArea, '.2f'), triUnit)