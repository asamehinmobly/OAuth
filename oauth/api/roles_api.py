from flask import Response, request
from gateway.db import session_scope
from repositories.roles import RoleRepository
from utils import json
from http import HTTPStatus
from utils.validation_helper import __is_duplicated_data


def create_role(app_id):
    try:
        role_repository = RoleRepository()
        with session_scope() as session:
            data = request.get_json()
            is_duplicated, error_message = __is_duplicated_data(session, role_repository, app_id, data)
            if is_duplicated:
                return Response(response=json.dumps({"errors": error_message}),
                                status=HTTPStatus.CONFLICT.value, mimetype='application/json')
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

            is_duplicated, error_message = __is_duplicated_data(session, role_repository, app_id, data, role_id)
            if is_duplicated:
                return Response(response=json.dumps({"errors": error_message}),
                                status=HTTPStatus.CONFLICT.value, mimetype='application/json')

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


def get_permission_data(app_id, role_id):
    try:
        role_repository = RoleRepository()
        permissions = role_repository.get_permissions(app_id, role_id)
        return Response(response=json.dumps(permissions),
                        status=HTTPStatus.OK.value, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.NOT_FOUND.value, mimetype='application/json')
