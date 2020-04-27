from flask import Response, request
from repositories.resources import ResourceRepository
from utils import json
from http import HTTPStatus


def create_resource(app_id):
    try:
        resource_repository = ResourceRepository()
        data = request.get_json()
        is_duplicated, error_message = resource_repository.is_duplicated_data(app_id, data)
        if is_duplicated:
            return Response(response=json.dumps({"errors": error_message}),
                            status=HTTPStatus.CONFLICT.value, mimetype='application/json')
        data['app_id'] = app_id
        resource = resource_repository.create(**data)
        return Response(response=json.dumps(resource),
                        status=HTTPStatus.CREATED.value, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')


def update_resource(app_id, resource_id):
    try:
        resource_repository = ResourceRepository()
        data = request.get_json()

        is_duplicated, error_message = resource_repository.is_duplicated_data(app_id, data, resource_id)
        if is_duplicated:
            return Response(response=json.dumps({"errors": error_message}),
                            status=HTTPStatus.CONFLICT.value, mimetype='application/json')

        resource = resource_repository.update(resource_id, app_id, **data)
        return Response(response=json.dumps(resource),
                        status=HTTPStatus.ACCEPTED.value, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors:": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')


def list_resources(app_id):
    try:
        resource_repository = ResourceRepository()
        resources = resource_repository.list(app_id)
        return Response(response=json.dumps(resources),
                        status=HTTPStatus.OK, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')


def delete_resource(app_id, resource_id):
    try:
        resource_repository = ResourceRepository()
        resource_repository.delete(resource_id, app_id)
        return Response(response="",
                        status=HTTPStatus.NO_CONTENT, mimetype='application/json')

    except Exception as err:
        if 'message' not in err.__dict__:
            err.message = repr(err)
        print(err.__dict__, '\n\n')
        return Response(response=json.dumps({"errors": err.message}),
                        status=HTTPStatus.BAD_REQUEST.value, mimetype='application/json')
