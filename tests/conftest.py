import pytest
import json

from pathlib import Path

from nodels.kube.parsers import BaseParser


@pytest.fixture()
def node_data_str():
    parent = Path(__file__).parent
    p = parent / Path("node_data/nodes.json")
    print(p.resolve())
    return open(p.resolve()).read()


@pytest.fixture()
def node_data(node_data_str):
    return json.loads(node_data_str)


@pytest.fixture()
def node1_data():
    parent = Path(__file__).parent
    p = parent / Path("node_data/node1.json")
    return open(p.resolve()).read()


@pytest.fixture()
def node1(node1_data):
    return BaseParser(node_data=node1_data)
