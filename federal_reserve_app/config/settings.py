class BaseConfig(object):
    """Base configuration."""
    PROJECT = "Funding Circle Fred Data"
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    DATABASE_URI = 'postgresql://scott:tiger@postgres/fundingcircle'
    SCHEMA = 'fred'


