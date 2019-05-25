from .base import BaseGather


class Nodes(BaseGather):
    """
    Class that gathers node information about the kubernetes
    cluster we are either currently running in or currently selected as
    the current context
    """

    def gather(self):
        """ Gather node information """
        pass

    def report(self, url):
        pass

