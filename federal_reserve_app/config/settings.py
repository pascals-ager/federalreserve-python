class BaseConfig(object):
    """Base configuration."""
    PROJECT = "Funding Circle Fred Data"
    SECRET_KEY = 'thisissecret'
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://scott:tiger@postgres/fundingcircle'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'thisisdevsecret'
    SALT_KEY = 'saltthisthing'
