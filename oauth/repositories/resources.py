from oauth.models.resource import Resource
from oauth.repositories.base import BaseRepository


class ResourceRepository(BaseRepository):
    Model = Resource
    ModelName = "resource"
    validator = None

    def __init__(self):
        pass
