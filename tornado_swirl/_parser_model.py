"""Parser FSM models."""


class PathSpec(object):
    """Represents the path specification of an REST API endpoint."""

    def __init__(self):
        self.summary = ""
        self.description = ""
        self.query_params = {}
        self.path_params = {}
        self.body_params = {}
        self.header_params = {}
        self.form_params = {}
        self.cookie_params = {}
        self.responses = {}
        self.properties = {}
        self.tags = {}
        self.deprecated = False
        self.security = {}


class SchemaSpec(object):
    """Represents a REST API component schema."""

    def __init__(self):
        self.name = ""
        self.summary = ""
        self.description = ""
        self.deprecated = False
        self.properties = {}
        self.example = None
        self.examples = None


class Param(object):
    """REST API section parameter"""

    def __init__(self, name, dtype='string', ptype='path',
                 required=False, readwrite=None, description=None, order=0):
        self.name = name
        self.type = dtype
        self.ptype = ptype
        self.required = required
        self.readwrite = readwrite
        self.description = description
        self.order = order
        self.kwargs = {}
        