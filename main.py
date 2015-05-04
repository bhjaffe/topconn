__author__ = 'Brian'

from ship import Ship


def ship_info(ship):
	# print '{:20s} {:20s} {:20s}'.format("COURSE", "SPEED", "RUDDER")
	print '{:15s} {:15s} {:15s}'.format(str(ship.course), str(ship.speed), str(ship.rudder_angle))
	# print 'Ship course: ' + str(ship.course)
	# print 'Ship speed:  ' + str(ship.speed)
	# print 'Ship rudder: ' + str(ship.rudder_angle)

def new_course_speed_rudder(ship, course, speed, rudder):
	ship.set_new_course(course)
	ship.set_new_speed(speed)
	ship.set_new_rudder_angle(rudder)

def one_second(ship):
	ship.change_speed()
	ship.change_rudder_angle()
	ship.change_course()


# ***************************************************************
#    TEST SCENARIO
# ***************************************************************

myShip = Ship(90, 15)

print '{:15s} {:15s} {:15s}'.format("COURSE", "SPEED", "RUDDER")
ship_info(myShip)
new_course_speed_rudder(myShip, 180, 20, 10)
for i in range(60):
	one_second(myShip)
	ship_info(myShip)

