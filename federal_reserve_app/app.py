from flask import Flask
from api import fredApi
import os
from celery import Celery


CELERY_TASK_LIST = [
    'api.tasks',
]

def create_celery_app(app=None):
    """
    Create a new Celery object and tie together the Celery config to the app's
    config. Wrap all tasks in the context of the application.

    :param app: Flask app
    :return: Celery app
    """
    app = app or create_app()

    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'],
                    include=CELERY_TASK_LIST)
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery

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



