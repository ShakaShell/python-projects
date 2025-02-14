#Michael Roberts
#Section 11
#On my honor, I have neither received nor given any unauthorized assistance on this assignment.

#Part 1: Painting

import math
numRooms = input("How many rooms need to be painted?")
numRooms = int(numRooms)

extraCoat = input("Would you like to get a third coat of paint?")
withExtraCoat = 0

if extraCoat == "Yes" or  extraCoat == "yes":
    basePaintCost = math.ceil(300 * numRooms)
    withExtraCoat = math.ceil(basePaintCost + (basePaintCost * .30))
    print("The total cost for", numRooms, "rooms with an extra coat of paint is: $", withExtraCoat)
else:
    basePaintCost = math.ceil(300 * numRooms)
    print("The total cost for", numRooms, "rooms without an extra coat of paint is: $", basePaintCost)


#Part 2: Ductwork

lengthRoom = input("What is the length of your living room?")
widthRoom = input("What is the width of your living room?")

lengthRoom = int(lengthRoom)
widthRoom = int(widthRoom)
 
diagonalSize = math.sqrt((lengthRoom ** 2) + (widthRoom ** 2))
diagonalSize = float(diagonalSize)

print("Diagonal distance for your living room is:", diagonalSize, "feet.")

if diagonalSize < 20:
    cutCorners = input("Would you like us to cut corners and route the ductwork diagonally to save money?")
    if cutCorners == "Yes" or cutCorners == "yes":
        diagonalCost = int(400 + (10 * diagonalSize))
        print("The cost of the ductwork ran diagonally is $", diagonalCost)
    else:
        regDuctCost =int(400 + 10 * (lengthRoom + widthRoom))
        print("The cost of the ductwork is $", regDuctCost)
else:
    regDuctCost =int(400 + 10 * (lengthRoom + widthRoom))
    print("The cost of the ductwork is $", regDuctCost)

#Part 3: Flooring

floorSize = input("What is the square footage of your house?")
floorSize = int(floorSize)

if floorSize < 1000:
    floorCost =int(8 * floorSize)
    print("The cost to install flooring is $", floorCost)
else: 
    if floorSize >= 1000 and floorSize < 3000:
        floorCost =int(6 * floorSize)
        print("The cost to install flooring is $", floorCost)
    else:
        floorCost =int(4 * floorSize)
        print("The cost to installing flooring is $", floorCost)



#Part 4: Totals

if withExtraCoat > 0 and diagonalCost > 0:
    totalCost = (withExtraCoat + diagonalCost + floorCost)
else:
    if withExtraCoat > 0 and diagonalCost == 0:
        totalCost = (withExtraCoat + regDuctCost + floorCost)
    else:
        if withExtraCoat == 0 and diagonalCost > 0:
            totalCost = (basePaintCost + diagonalCost + floorCost)
        else:
            totalCost = (basePaintCost + regDuctCost + floorCost)

print("The total cost of the remodeling of your home is $", int(totalCost))






