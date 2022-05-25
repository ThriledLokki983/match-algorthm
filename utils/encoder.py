from json import JSONEncoder, loads


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

# add decode attribute to JSONEncoder


def decode(json_string):
    return loads(json_string)
