import json

class JSONSerializer(object):
    def serialize(self, obj):
        return json.dumps(obj)

    def deserialize(self, string):
        return json.loads(string)
