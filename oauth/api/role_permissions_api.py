from flask import Response, request
from repositories.role_permission import RolePermissionRepository
from utils import json
from http import HTTPStatus


def add_permission(app_id, role_id):
    try:
        role_permission_repository = RolePermissionRepository()
        data = request.get_json()
        data['role_id'] = role_id
        role_permission = role_permission_repository.create(app_id, **data)
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
        role_permission = role_permission_repository.get(**{"role_id": role_id})
        return Response(response=json.dumps(role_permission),
                        status=HTTPStatus.OK.value, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')


def delete_permission(app_id, role_id, permission_id):
    try:
        role_permission_repository = RolePermissionRepository()
        role_permission_repository.delete(app_id, role_id, permission_id)
        return Response(response="",
                        status=HTTPStatus.NO_CONTENT.value, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')
