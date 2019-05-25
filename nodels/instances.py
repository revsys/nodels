import json


class Instances:
    """
    Class that gathers cloud instance information.

    If `region` is defined it will only gather instance information from that
    particular region.  By default region is None and it will gather instance
    information for ALL regions
    """

    def __init__(self, region=None, data=None):
        self.region = region
        self.data = data
        if self.data is None:
            self.data = {}

    def to_dict(self):
        return self.data

    def gather(self):
        pass

    def json(self, pretty=False):
        return json.dumps(self.to_dict())

    def report(self, url):
        pass
