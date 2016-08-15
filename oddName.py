"""
Jose Oronos
"""

name = input("What is your name?: ")
while name == "":
    name = input("Error, try again: ")
for c in name[1:len(name):2]:
    print(c, end=" ")
