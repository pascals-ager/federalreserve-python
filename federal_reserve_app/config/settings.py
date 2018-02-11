class BaseConfig(object):
    """Base configuration."""
    PROJECT = "Funding Circle Fred Data"
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SECRET_KEY = 'ThisIsMySecretKey'
    DATABASE_URI = 'postgresql://scott:tiger@postgres/fundingcircle'
    SCHEMA = 'fred'
    API_KEY = 'bf7e372a4731983197a88028a0d6c23c'
    CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'  #0 at the end is the default database at redis.
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_REDIS_MAX_CONNECTIONS = 5
    LOG_LEVEL = 'DEBUG'


