from flask import Flask
from api import fredApi


def create_app():

    '''
    This is the application factory which returns the flask app object.
    The config_name directs a runtime configuration load.
    '''
    app = Flask(__name__)    
    app.config.from_object('config.settings.DevelopmentConfig')    
    app.register_blueprint(fredApi)    

    return app

'''
if __name__=='__main__':    
    app = create_app()  # os.environ['ENV_SETTINGS']; export ENV_SETTINGS='DevelopmentConfig'
    
    app.run(debug=True)
'''

