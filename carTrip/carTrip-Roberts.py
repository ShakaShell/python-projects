#Michael Roberts
#Section 11
#On my honor, I have neither received nor given any unauthorized assistance on this assignment
import math

Mpg = 20
TankSize = 10
TripDistance = 400

DistancePossible = Mpg * TankSize
#calculates the total mileage the car can travel

MakeTrip = DistancePossible >= TripDistance
#determines if the distance of the trip is longer than the distance the car is capable of

print("Mpg: ", Mpg)
print("TankSize: ", TankSize)
print("Trip Distance: ", TripDistance)
print("I can make the trip on one tank of gas: ", MakeTrip)



