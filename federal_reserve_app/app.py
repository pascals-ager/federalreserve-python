from flask import Flask
from api import fredApi
import os


def create_app():

    '''
    This is the application factory which returns the flask app object.
    The config_name directs a runtime configuration load.
    '''
    config_name = os.environ['ENV_SETTINGS']
    config_object = ".".join(('config.settings',config_name))
    app = Flask(__name__)    
    app.config.from_object(config_object)    
    app.register_blueprint(fredApi)    

    return app

'''
if __name__=='__main__':    
    app = create_app()  # os.environ['ENV_SETTINGS']; export ENV_SETTINGS='DevelopmentConfig'
    
    app.run(debug=True)
'''

