from flask import Flask
#from extensions import db
from api import gdpApi


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
    
    
    app.register_blueprint(gdpApi)    
    #app.register_blueprint(signApi)
    #app.register_blueprint(serviceApi)

    return app


if __name__=='__main__':    
    app = create_app()  # os.environ['ENV_SETTINGS']; export ENV_SETTINGS='DevelopmentConfig'
    
    app.run(debug=True)


