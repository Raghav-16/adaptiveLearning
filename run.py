#imports everything from the application folder
from application import app

app.secret_key = 'Raghav!@#$%'

#starts the server, debug mode is off
app.debug = False
app.run()
