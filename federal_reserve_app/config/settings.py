class BaseConfig(object):
    """Base configuration."""
    PROJECT = "Funding Circle Fred Data"
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://scott:tiger@localhost:5432/fundingcircle'


