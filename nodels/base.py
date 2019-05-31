import datetime
import json

from dataclasses import dataclass


def json_encoder(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


class BaseGather:
    """
    Base class for our gatheres that implements some common logic
    """

    def __init__(self, data=None):
        self.data = data
        if self.data is None:
            self.data = {}

    def to_dict(self):
        return dict(self.data)

    def gather(self):
        raise NotImplementedError("gather needs to be defined in subclass")

    def json(self, pretty=False):
        sort_keys = False
        indent = None
        if pretty:
            sort_keys = True
            indent = 2

        return json.dumps(
            self.to_dict(), sort_keys=sort_keys, indent=indent, default=json_encoder
        )

    def report(self, url):
        raise NotImplementedError("report needs to be defined in subclass")


@dataclass
class Report:
    """
    Small class to handle our reports back to the API
    """

    data: dict

    def to_dict(self):
        return self.data

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2, default=json_encoder)
