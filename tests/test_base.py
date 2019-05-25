import pytest

from nodels.base import BaseGather


def test_to_dict():
    b = BaseGather()
    assert b.to_dict() == {}

    b2 = BaseGather(data={"foo": "bar"})
    assert b2.to_dict() == {"foo": "bar"}


def test_json():
    b = BaseGather()
    assert b.json() == "{}"

    b2 = BaseGather(data={"foo": "bar"})
    assert b2.json() == '{"foo": "bar"}'


def test_gather_raises():
    b = BaseGather()
    with pytest.raises(NotImplementedError):
        b.gather()


def test_report_raises():
    b = BaseGather()
    with pytest.raises(NotImplementedError):
        b.report(url="")
