from ..base import BaseGather, Report


class Instances(BaseGather):
    """
    Class that gathers cloud instance information.

    If `region` is defined it will only gather instance information from that
    particular region.  By default region is None and it will gather instance
    information for ALL regions
    """

    def __init__(self, region=None, data=None):
        super().__init__(data=data)
        self.region = region

    def gather(self):
        pass

    def generate_report(self, name=None, id=None):
        """ Format our report data """
        data = {"name": name, "id": id, "instances": []}
        report = Report(data=data)
        return report

    def report(self, url, token, name=None, id=None):
        report = self.generate_report(name, id)
        return report

