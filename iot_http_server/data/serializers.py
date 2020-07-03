from django.db.models import QuerySet
from data.models import Data, State


def serialize_data_queryset(data: QuerySet(Data)) -> str:
    out: str = "["
    for i in data:
        out += i.serialize_to_json()
        out += ","
    out += "]"
    return out


def serialize_data_single(data: Data) -> str:
    out: str = "["
    out += data.serialize_to_json()
    out += "]"
    return out
