
def __is_duplicated_data(session, repository, app_id, data, obj_id=None):
    obj = repository.get(session, app_id, name=data['name'])
    if obj:
        if not obj_id or obj_id != obj[0].get('id'):
            return True, 'name must be unique'
    return False, ''


# def __validate(data):
#     return validate(instance=data, schema=body_schema)
