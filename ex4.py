#encoding=utf-8
#变量

cars = 100
space_in_a_car = 4.0
drivers = 30
passerngers = 90
cars_not_drivern = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passerngers / cars_driven


print "There are",cars,"cars available."      #打印一个变量
print "There are %d cars available" % cars    #打印一个变量
print "There are %d cars available and %d drivers available" % (cars,drivers)  #打印多个变量
print "There are only",drivers,"drivers available."
print "There will be",cars_not_drivern,"empty cars today."
print "we can transport",carpool_capacity,"people today."
print "We have",passerngers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."


'''
result:

There are 100 cars available.
There are 100 cars available
There are 100 cars available and 30 drivers available
There are only 30 drivers available.
There will be 70 empty cars today.
we can transport 120.0 people today.
We have 90 to carpool today.
We need to put about 3 in each car.


'''
