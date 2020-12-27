from flask import Flask, render_template
from flask import make_response
from flask import request
import random
from datetime import datetime
import socket

from flask.globals import request
app = Flask(__name__)


@app.route("/")
def index():
    rangenumbers = range(1,13)
    bgcolor = random.choice( ['orange', 'green', 'purple'] )
    cookie_color = request.cookies.get('color')
    hostname = socket.gethostname()

    if cookie_color is not None:
        bgcolor = cookie_color

        response = make_response(
            render_template(
                'index.html', 
                the_date=datetime.now(),
                numbers=rangenumbers,
                css_bg=bgcolor,
                hostname=hostname))        
    else: 
        response = make_response(
            render_template(
                'index.html', 
                the_date=datetime.now(),
                numbers=rangenumbers,
                css_bg=bgcolor,
                hostname=hostname))
        response.set_cookie('color', bgcolor)  
    
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
