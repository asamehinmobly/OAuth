import warnings

from future.utils import with_metaclass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Credentials(with_metaclass(Singleton)):
    def __init__(self, credentials_dict=None):
        if getattr(self, '__credentials', None):
            warnings.warn("Credentials are already set. ignoring the provided credentials", UserWarning)
        else:
            self.__credentials = credentials_dict

    @staticmethod
    def get_credentials():
        return Singleton._instances.get(Credentials).credentials

    @staticmethod
    def set_credentials(credentials_dict=None):
        Credentials(credentials_dict=credentials_dict)
        return Credentials.get_credentials()

    @staticmethod
    def clear():
        try:
            Singleton._instances.pop(Credentials)
        except:
            pass

    @property
    def credentials(self):
        if not self.__credentials:
            warnings.warn("Credentials are not set", UserWarning)
        return self.__credentials
