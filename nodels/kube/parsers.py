import json

from dateutil.parser import parse as date_parser
from jsonpath_rw import parse


class BaseParser:
    """
    Default Kubernetes parser
    """

    def __init__(self, node_data):
        self.data = self._load_data(node_data)

    def _load_data(self, node_data):
        """
        If the data is a string, assume it's valid JSON, otherwise ensure
        it's a dictionary in the proper form
        """
        # If we're a string, load it up
        if isinstance(node_data, str):
            return json.loads(node_data)

        # Otherwise it should be a dictionary containing a single node
        if not isinstance(node_data, dict):
            raise ValueError("node_data is not a JSON string or dictionary")

        return node_data

    def get(self, path):
        matches = parse(path).find(self.data)

        if not len(matches):
            return None

        if len(matches) > 1:
            return [m.value for m in matches]

        return matches[0].value

    def name(self, json_path="$.metadata.name"):
        """ Retrieve the name from `metadata.name` """
        return self.get(json_path)

    def external_id(self, json_path="$.spec.external_id"):
        """ Return the node's external ID """
        return self.get(json_path)

    def created(self, json_path="$.metadata.creation_timestamp"):
        """ Return this node's creation timestamp as a datetime """
        date_str = self.get(json_path)

        if date_str is None:
            return None

        return date_parser(date_str)

    def size(self, json_path='$.metadata.labels."beta.kubernetes.io/instance-type"'):
        return self.get(json_path)
