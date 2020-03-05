from flask import Response, request
from oauth.gateway.db import session_scope
from oauth.repositories.roles import RoleRepository
from oauth.utils import json
from http import HTTPStatus


def list_roles(app_id):
    try:
        role_repository = RoleRepository()
        with session_scope() as session:
            ads = role_repository.list(session, app_id)
            return Response(response=json.dumps(ads),
                            status=HTTPStatus.OK, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')
