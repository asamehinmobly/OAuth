import json
from datetime import date, datetime


def default_converter(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()


def dumps(data):
    return json.dumps(data, default=default_converter)
