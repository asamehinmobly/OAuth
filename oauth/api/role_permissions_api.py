from flask import Response, request
from oauth.gateway.db import session_scope
from oauth.repositories.role_permission import RolePermissionRepository
from oauth.utils import json
from http import HTTPStatus


def add_permission(app_id, role_id):
    try:
        role_permission_repository = RolePermissionRepository()
        with session_scope() as session:
            data = request.get_json()
            data['role_id'] = role_id
            role_permission = role_permission_repository.create(session, **data)
            return Response(response=json.dumps(role_permission),
                            status=HTTPStatus.OK.value, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')


def get_permissions(app_id, role_id):
    try:
        role_permission_repository = RolePermissionRepository()
        with session_scope() as session:
            data = request.get_json()
            data['role_id'] = role_id
            role_permission = role_permission_repository.create(session, **data)
            return Response(response=json.dumps(role_permission),
                            status=HTTPStatus.OK.value, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')


def delete_permission(app_id, role_id, ):
    try:
        role_permission_repository = RolePermissionRepository()
        with session_scope() as session:
            data = request.get_json()
            data['role_id'] = role_id
            role_permission = role_permission_repository.create(session, **data)
            return Response(response=json.dumps(role_permission),
                            status=HTTPStatus.OK.value, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')
