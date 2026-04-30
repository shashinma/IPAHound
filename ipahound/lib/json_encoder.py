import json


class ExtendedEncoder(json.JSONEncoder):

    def default(self, obj):
        name = type(obj).__name__
        try:
            encoder = getattr(self, f'encode_{name}')
        except AttributeError:
            super().default(obj)
        else:
            encoded = encoder(obj)
            return encoded

    @staticmethod
    def encode_bytes(obj):
        return str(obj)

    @staticmethod
    def encode_datetime(obj):
        return obj.strftime('%H:%M:%S %d.%m.%Y')
