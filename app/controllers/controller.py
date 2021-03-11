from flask import render_template, request, redirect# ADDED
from app import app
from app.models.events_list import events, add_new_event
from app.models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title="Events Planner", events=events)

@app.route('/events', methods=['POST'])
def create():
    event_date = request.form['date']
    event_name = request.form['name']
    event_guests =  request.form['guests']
    event_location = request.form['location']
    event_description = request.form['description']
    new_event = Event(event_date, event_name, event_guests, event_location, event_description)
    add_new_event(new_event)
    return redirect('/events')