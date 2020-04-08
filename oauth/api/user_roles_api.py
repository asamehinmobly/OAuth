from flask import Response
from repositories.user_role import UserRoleRepository
from utils import json
from http import HTTPStatus


def get_roles(user_id):
    try:
        user_role_repository = UserRoleRepository()
        user_roles = user_role_repository.get(**{"user_id": user_id})
        return Response(response=json.dumps(user_roles),
                        status=HTTPStatus.OK, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')
