from django.db.models import QuerySet
from data.models import Data, State


def serialize_data_queryset(data: QuerySet(Data)) -> str:
    if not data:
        return "[]"
    out: str = "["
    for i in data:
        out += i.serialize_to_json()
        out += ","
    out += "]"
    return out


def serialize_data_single(data: Data) -> str:
    if not data:
        return "[]"
    out: str = "["
    out += data.serialize_to_json()
    out += "]"
    return out


def serialize_state_queryset(data: QuerySet(State)) -> str:
    if not data:
        return []
    out: str = "["
    for i in data:
        out += i.serialize_to_json()
        out += ","
    out += "]"
    return out


def serialize_state_single(data: State) -> str:
    if not data:
        return "[]"
    out: str = "["
    out += data.serialize_to_json()
    out += "]"
    return out
