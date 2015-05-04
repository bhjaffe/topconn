__author__ = 'Brian'

class Ship(object):
	def __init__(self, course, speed):
		self.course = course
		self.course_ordered = course
		self.speed = speed
		self.speed_ordered = speed
		self.rudder_angle = 0.0
		self.rudder_angle_ordered = 0.0
		self.rate_speed_change = 0.2 # knots / second
		self.rate_rudder_change = 2.0 # degrees / second
		self.rate_course_change = 0.02 # degrees / (knots_of_speed * degrees_of_rudder * second)
		self.time_rudder_ease = 5.0 # seconds looking ahead to reduce turn rate to not overshoot desired course
		self.rudder_angle_reduction_factor = 1.5 # factor by which rudder angle is reduced when overshoot is approaching

	@staticmethod
	def correct_360_math(number_of_degrees): # corrects for 359 + 1 degrees = 0 degrees, etc.
		if number_of_degrees >= 360:
			return number_of_degrees - 360
		if number_of_degrees < 0:
			return number_of_degrees+ 360
		return number_of_degrees

	def set_new_course(self, new_course):
		self.course_ordered = new_course

	def set_new_rudder_angle(self, new_rudder_angle):
		self.rudder_angle_ordered = new_rudder_angle

	def set_new_speed(self, new_speed):
		self.speed_ordered = new_speed

	def change_rudder_angle(self):
		if self.rudder_angle != 0:
			seconds_to_overshoot = self.correct_360_math(self.course_ordered - self.course) / (self.speed*self.rudder_angle*self.rate_course_change) # number of seconds at current turn rate until ship overshoots turn
		else:
			seconds_to_overshoot = 999
		if seconds_to_overshoot < self.time_rudder_ease:
			self.rudder_angle = self.rudder_angle / self.rudder_angle_reduction_factor
			self.rudder_angle_ordered = self.rudder_angle
		elif self.rudder_angle != self.rudder_angle_ordered: # increase abs(rudder_angle) to increase turn rate
			if self.rudder_angle_ordered > self.rudder_angle:
				self.rudder_angle += self.rate_rudder_change
			else:
				self.rudder_angle -= self.rate_rudder_change

	def change_speed(self):
		if self.speed != self.speed_ordered:
			if self.speed_ordered > self.speed:
				self.speed += self.rate_speed_change
			else:
				self.speed -= self.rate_speed_change
		if abs(self.speed - self.speed_ordered) <= 0.2:
			self.speed = self.speed_ordered

	def change_course(self):
		self.course = self.correct_360_math(self.course + self.speed*self.rudder_angle*self.rate_course_change)
		if abs(self.course - self.course_ordered) < 1.0:
			self.course = self.course_ordered
			self.rudder_angle = 0.0
			self.rudder_angle_ordered = 0.0

