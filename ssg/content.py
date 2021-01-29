import re
from typing import _KT, _VT_co

from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    def __getitem__(self, k):
        return self.data[k]

    def __iter__(self):
        return self.data.__iter__()

    def __repr__(self):
        data = {}
        for key, value in self.data:
            if key != 'content':
                data[key] = value
        return str(data)

    def __len__(self):
        return len(self.data)

    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = cls._regex.split(string, 2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data['content'] = content

    @property
    def body(self):
        return self.data['content']\


    @property
    def type(self):
        return self.data['type']

    @type.setter
    def type(self, type):
        self.data['type'] = type






