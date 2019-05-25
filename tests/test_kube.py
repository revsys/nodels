from nodels.kube import Nodes


def test_to_dict():
    n = Nodes()
    assert n.to_dict() == {}

    n2 = Nodes(data={"foo": "bar"})
    assert n2.to_dict() == {"foo": "bar"}


def test_json():
    n = Nodes()
    assert n.json() == "{}"

    n2 = Nodes(data={"foo": "bar"})
    assert n2.json() == '{"foo": "bar"}'
