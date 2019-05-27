import datetime
import pytest
from nodels.kube.parsers import BaseParser


def test_load_data_str(node_data_str):
    b = BaseParser(node_data=node_data_str)
    assert isinstance(b.data, dict)


def test_load_data_dict(node_data):
    b = BaseParser(node_data=node_data)
    assert isinstance(b.data, dict)


def test_incorrect_loading():
    with pytest.raises(ValueError):
        BaseParser(node_data="")

    with pytest.raises(ValueError):
        BaseParser(node_data=[])

    b = BaseParser(node_data="{}")
    assert isinstance(b, BaseParser)


def test_name(node1):
    assert node1.name() == "ip-10-131-10-138.us-west-2.compute.internal"


def test_external_id(node1):
    assert node1.external_id() == "i-09587a5ad7a5d60f3"


def test_created(node1):
    assert isinstance(node1.created(), datetime.datetime)


def test_size(node1):
    assert node1.size() == "r5.xlarge"


def test_kind(node1):
    assert node1.kind() == "node"


def test_region(node1):
    assert node1.region() == "us-west-2"


def test_node_kwargs(node1):
    kwargs = node1.node_kwargs()
    # Spot check the kwargs
    assert kwargs["name"] == "ip-10-131-10-138.us-west-2.compute.internal"
    assert kwargs["region"] == "us-west-2"
    assert kwargs["data"] == node1.data
