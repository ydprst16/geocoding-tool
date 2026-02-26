import json
import os

class Cache:
    def __init__(self, path):
        self.path = path
        self.data = self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                return json.load(f)
        return {}

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f)

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value