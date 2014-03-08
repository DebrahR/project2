""" main.py is the top level script.

Return "Hello World" at the root URL.
"""

import os
import webapp2

import sys
# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import render_template
app = Flask(__name__.split('.')[0])
                                       
@app.route('/')
@app.route('/')
def cards(name=None):
  """ Return me template at application /me URL."""
  return render_template('cards.html', name=name)


