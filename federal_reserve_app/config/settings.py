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


