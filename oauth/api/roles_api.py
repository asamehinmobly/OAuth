from flask import Response, request
from oauth.gateway.db import session_scope
from oauth.repositories.roles import RoleRepository
from oauth.utils import json
from http import HTTPStatus


def create_role(app_id):
    try:
        role_repository = RoleRepository()
        with session_scope() as session:
            data = request.get_json()
            data['app_id'] = app_id
            role = role_repository.create(session, **data)
            return Response(response=json.dumps(role),
                            status=HTTPStatus.CREATED.value, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')


def update_role(app_id, role_id):
    try:
        role_repository = RoleRepository()
        with session_scope() as session:
            data = request.get_json()
            role = role_repository.update(session, role_id, app_id, **data)
            return Response(response=json.dumps(role),
                            status=HTTPStatus.ACCEPTED.value, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors:": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')


def list_roles(app_id):
    try:
        role_repository = RoleRepository()
        with session_scope() as session:
            roles = role_repository.list(session, app_id)
            return Response(response=json.dumps(roles),
                            status=HTTPStatus.OK, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')


def delete_role(app_id, role_id):
    try:
        role_repository = RoleRepository()
        with session_scope() as session:
            role_repository.delete(session, role_id, app_id)
            return Response(response="",
                            status=HTTPStatus.NO_CONTENT, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')
