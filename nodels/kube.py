import json


class Nodes:
    """
    Class that gathers node information about the kubernetes
    cluster we are either currently running in or currently selected as
    the current context
    """

    def __init__(self, data=None):
        self.data = data
        if self.data is None:
            self.data = {}

    def to_dict(self):
        return self.data

    def gather(self):
        """ Gather node information """
        pass

    def json(self, pretty=False):
        """ Return node data in JSON format """
        return json.dumps(self.to_dict())

    def report(self, url):
        pass

