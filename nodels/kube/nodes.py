import datetime
from dataclasses import dataclass

from kubernetes import client, config

from ..base import BaseGather

from .parsers import BaseParser


@dataclass
class Node:
    """
    Class to represent a single Kubernetes node
    """

    name: str
    external_id: str
    created: datetime.datetime
    size: str
    kind: str
    region: str
    zone: str
    data: dict


class Nodes(BaseGather):
    """
    Class that gathers node information about the kubernetes
    cluster we are either currently running in or currently selected as
    the current context
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = self.get_client()
        self.name = kwargs.get("cluster_name", None)
        self.id = kwargs.get("cluster_reporting_id", None)
        self.nodes = []

    def get_client(self):
        config.load_kube_config()
        return client.CoreV1Api()

    def get_node_data(self):
        return self.client.list_node(pretty=True, limit=500)

    def gather(self):
        """ Gather node information """
        kube_data = []
        nodes = []
        node_data = self.get_node_data()

        for node in node_data.items:
            node_dict = node.to_dict()
            kube_data.append(node_dict)
            b = BaseParser(node_data=node_dict)
            node_kwargs = b.node_kwargs()
            nodes.append(Node(**node_kwargs))

        self.data["nodes"] = kube_data
        self.nodes = nodes

    def report(self, url):
        pass
