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


def test_add_node(node1_data):
    n = Nodes()
    n.add_node(node1_data)


def test_generate_report(node1_data):
    n = Nodes()
    n.add_node(node1_data)

    data = n.generate_report(name="testing", id="1234")

    assert data["id"] == "1234"
    assert data["name"] == "testing"
    assert len(data["nodes"]) == 1
    assert data["nodes"][0]["external_id"] == "i-09587a5ad7a5d60f3"
