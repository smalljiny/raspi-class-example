from flask import Flask

from controllers.leds.controllers import leds

app = Flask(__name__)
app.debug = True

app.register_blueprint(leds, url_prefix='/leds')
