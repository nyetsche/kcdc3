"""This module provides a bunch of helper functions to deal with user
registration stuff."""

from models import Event, Registration
from django.contrib.auth.models import User
from datetime import datetime, timedelta


def is_waitlisted(student, event):
	"""Checks to see if a student is waitlisted for a given event."""
	if student == None:
		return False

	student_registrations = Registration.objects.filter(
					event=event, 
					student=student, 
					waitlist=True,
					cancelled=False)

	if len(student_registrations) > 0:
		return True
	else:
		return False

def is_registered(student, event):
	"""Checks to see if a student is registered for a given event."""
	if student == None:
		return False

	student_registrations = Registration.objects.filter(
					event=event, 
					student=student, 
					waitlist=False, 
					cancelled=False)	
	if len(student_registrations) > 0:
		return True
	else:
		return False

def is_cancelled(student, event):
	"""Checks to see if a student has cancelled for a given event."""
	if student == None:
		return False

	student_registrations = Registration.objects.filter(
					event=event,
					student=student,
					cancelled=False)

	if len(student_registrations) > 0:
		return False
	else:
		return True


def cancel_registration(student, event):
	"""Cancels the users registration for an event."""
	registration = Registration.objects.filter(
				event=event, 
				student=student, 
				cancelled=False)[0]
	registration.date_cancelled=datetime.now()
	registration.cancelled=True
	registration.save()

def promote_waitlistee(event):
	"""Promotes a waitlisted student to registered for an event."""
	registrations = Registration.objects.filter(
				event=event, 
				waitlist=True, 
				cancelled=False)

	if len(registrations) == 0:
		return None
	registration = registrations[0]
	print "registration: "+str(registration)

	registration.waitlist=False
	registration.date_promoted=datetime.now()
	
	registration.late_promotion=event.is_late_promotion
		
	registration.save()
	return registration.student
