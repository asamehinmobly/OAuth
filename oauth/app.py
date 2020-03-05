from flask import Flask

from werkzeug.utils import import_string, cached_property

from oauth.middlewares.api_decorators import oauth_checker

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

if __name__ == "__main__":
    app.run(port=8000)
