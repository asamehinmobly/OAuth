class IRepository(object):
    def create(self, **kwargs):
        pass

    def list(self, app_id):
        pass

    def get(self, app_id, **kwargs):
        pass

    def update(self, model_id, app_id, **kwargs):
        pass

    def delete(self, model_id, app_id):
        pass
