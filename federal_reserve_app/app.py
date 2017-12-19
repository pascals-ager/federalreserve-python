from flask import Flask
#from extensions import db
#from api import registerApi, signApi, serviceApi


def create_app():

    '''
    This is the application factory which returns the flask app object.
    The config_name directs a runtime configuration load.
    '''
    app = Flask(__name__)
    
    app.config.from_object('config.settings.DevelopmentConfig')
  

    '''
    initialize the db and register the modularized services to the app.
    '''
    #db.init_app(app)
    
    
    #app.register_blueprint(registerApi)    
    #app.register_blueprint(signApi)
    #app.register_blueprint(serviceApi)

    return app



