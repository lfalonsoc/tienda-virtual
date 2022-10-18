from flask import Flask
from config import Config

from .routs import glogal_h
# from .routs.routes import glogal_h

app=Flask(__name__,static_folder=Config.STATIC_FOLDER,template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

app.register_blueprint(glogal_h)

""" @app.route('/index')
@app.route('/')
def index():
  return 'Hola Mundo, cómo vais?' """