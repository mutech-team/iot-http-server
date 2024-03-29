from django.db.models import QuerySet
from mqtt.models import Data, State


def serialize(data):
    if not data:
        return "[]"
    try:
        if (type(data)) == QuerySet or (type(data)) == list:
            out = "["
            for i in data:
                out += i.serialize_to_json()
                out += ","
            out += "]"
            return out
        else:
            out = "["  # type: ignore
            out += data.serialize_to_json()
            out += "]"
            return out
    except AttributeError:
        print("Model that you want to serialize must have serialize_to_json() "
              "function, returning JSON trough json.dumps")
        return "[]"
