from app.models.event import *

event1 = Event("29rd of April", "Birth Woodland Rave", "17", "Stretches of the Forest", "Yet another year yet another rave")
event2 = Event("30th of October", "Lonely Tea Party", "3", "TBD", "Spill the tea")

events = [event1, event2]

def add_new_event(event):
    events.append(event)