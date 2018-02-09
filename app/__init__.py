#from flask import Flask
import os
from .flask_extended import Flask  #uses the local extension for supporting YAML

app = Flask(__name__)
#app.config.from_object('config')
config_path = os.path.dirname(app.root_path)
app.config.from_yaml(os.path.join(config_path, 'config.yaml'))

#from app import views
from app import views_boto
#from app import admin
