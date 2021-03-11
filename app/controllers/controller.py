from flask import render_template, request, redirect# ADDED
from app import app
from app.models.events_list import events, add_new_event
from app.models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title="Events Planner", events=events)