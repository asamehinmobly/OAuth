from flask import Flask
from werkzeug.utils import import_string, cached_property
from middlewares.api_decorators import oauth_checker

app = Flask('oauth')
app.config.from_object('settings')


class LazyView(object):
    middle_wares = [oauth_checker]

    def __init__(self, import_name, auth=True):
        self.__module__, self.__name__ = import_name.rsplit('.', 1)
        self.import_name = import_name
        self.auth = auth

    @property
    def view_with_middleware(self):
        view = self.view
        for middle_ware in reversed(self.middle_wares):
            view = middle_ware(view, self.auth)
        return view

    @cached_property
    def view(self):
        return import_string(self.import_name)

    def __call__(self, *args, **kwargs):
        response = self.view_with_middleware(*args, **kwargs)
        return response


# Actions
app.add_url_rule("/roles", methods=['GET'],
                 view_func=LazyView('api.roles_api.list_roles'))

app.add_url_rule("/roles", methods=['POST'],
                 view_func=LazyView('api.roles_api.create_role'))

app.add_url_rule("/roles/<string:role_id>", methods=['PUT'],
                 view_func=LazyView('api.roles_api.update_role'))

app.add_url_rule("/roles/<string:role_id>", methods=['DELETE'],
                 view_func=LazyView('api.roles_api.delete_role'))

app.add_url_rule("/roles/<string:role_id>/permissions", methods=['GET'],
                 view_func=LazyView('api.role_permissions_api.get_permissions'))

app.add_url_rule("/roles/<string:role_id>/permissions", methods=['POST'],
                 view_func=LazyView('api.role_permissions_api.add_permission'))

app.add_url_rule("/roles/<string:role_id>/permissions/<string:permission_id>", methods=['DELETE'],
                 view_func=LazyView('api.role_permissions_api.delete_permission'))

app.add_url_rule("/resources", methods=['GET'],
                 view_func=LazyView('api.resources_api.list_resources'))

app.add_url_rule("/resources", methods=['POST'],
                 view_func=LazyView('api.resources_api.create_resource'))

app.add_url_rule("/resources/<string:resource_id>", methods=['PUT'],
                 view_func=LazyView('api.resources_api.update_resource'))

app.add_url_rule("/resources/<string:resource_id>", methods=['DELETE'],
                 view_func=LazyView('api.resources_api.delete_resource'))

if __name__ == "__main__":
    app.run(port=80)
