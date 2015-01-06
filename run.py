#!flask/bin/python
from werkzeug.serving import run_simple
from app import app

app.run(debug = True)



