import os
import string
import socket as s

_MQTT_STRING_SEPARATOR = "Æ¸·¬"


def _contains_whitespace(param: str) -> bool:
    return True in [c in param for c in string.whitespace]


def _is_docker():
    path = '/proc/self/cgroup'
    return (
            os.path.exists('/.dockerenv') or
            os.path.isfile(path) and any('docker' in line for line in open(path))
    )


_host = "mutech.ivica.codes"
_port = 5056

if _is_docker():
    _host = "172.17.0.1"

_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
_socket.connect((_host, _port))


def _send(mqtt_topic: str, mqtt_payload: str) -> None:
    if not _contains_whitespace(mqtt_topic):
        message: str = mqtt_topic + _MQTT_STRING_SEPARATOR + mqtt_payload + _MQTT_STRING_SEPARATOR + "\n"
        try:
            _socket.send(message.encode("utf-8"))
        except s.error:
            raise BrokenPipeError


def publish(deviceid: str, state: str, message: str) -> None:
    topic = "/" + deviceid + "/" + state
    _send(topic, message)
