import pytest


class BadRequest(Exception):
    pass


def raise_bad_request():
    raise BadRequest


def test_raise_bad_request():
    with pytest.raises(BadRequest):
        raise_bad_request()
