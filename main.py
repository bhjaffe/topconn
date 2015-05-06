__author__ = 'Brian'

from ship import Ship


def ship_info(ship):
	print '{:15s} {:15s} {:15s}'.format(str(ship.course), str(ship.speed), str(ship.rudder_angle))

def new_course_speed_rudder(ship, course, speed, rudder):
	# sets desired course, speed, and rudder angle (for that turn)
	ship.set_new_course(course)
	ship.set_new_speed(speed)
	ship.set_new_rudder_angle(rudder)

def one_second(ship):
	# adjusts all ship attributes by 1 second change
	ship.change_speed()
	ship.change_rudder_angle()
	ship.change_course()

def seconds_pass(seconds):
	for i in range(seconds):
		one_second(myShip)
		ship_info(myShip)


# ***************************************************************
#    TEST SCENARIO
# ***************************************************************

myShip = Ship(90, 15)

print '{:15s} {:15s} {:15s}'.format("COURSE", "SPEED", "RUDDER")
ship_info(myShip)
new_course_speed_rudder(myShip, 180, 20, 10)
seconds_pass(60)
new_course_speed_rudder(myShip, 15, 10, -15)
seconds_pass(120)
new_course_speed_rudder(myShip, 225, 20, -10)
seconds_pass(20)
new_course_speed_rudder(myShip, 350, 20, 10)
seconds_pass(60)
new_course_speed_rudder(myShip, 999, 15, 15)
seconds_pass(90)
new_course_speed_rudder(myShip, 999, 10, -20)
seconds_pass(90)