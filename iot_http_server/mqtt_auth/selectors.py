# Contains mypy-typed functions which query the ORM.
# Watch this https://www.youtube.com/watch?v=yG3ZdxBb1oo to understand.
import json


def auth_user(body: str) -> bool:
    return True


def auth_superuser(body: str) -> bool:
    return True


def auth_topic(body: str) -> bool:
    return True
