from kubernetes import client, config

from .base import BaseGather


class Nodes(BaseGather):
    """
    Class that gathers node information about the kubernetes
    cluster we are either currently running in or currently selected as
    the current context
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = self.get_client()

    def get_client(self):
        config.load_kube_config()
        return client.CoreV1Api()

    def get_node_data(self):
        return self.client.list_node(pretty=True, limit=500)

    def gather(self):
        """ Gather node information """
        kube_data = []
        node_data = self.get_node_data()

        for node in node_data.items:
            kube_data.append(node.to_dict())

        self.data["nodes"] = kube_data

    def report(self, url):
        pass

