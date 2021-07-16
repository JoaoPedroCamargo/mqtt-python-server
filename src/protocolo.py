import json
from src.documents import ProtocolDoc


class Protocol:
    def __init__(self, source="", to="", message="", event=""):
        self.source = source
        self.to = to
        self.message = message
        self.event = event

    def from_json(self, payload):
        try:
            message = json.loads(payload)["data"]
            keys = list(message.keys())

            key_self = ["to", "message"]

            for key in key_self:
                if not key in keys:
                    return

            self.to = message["to"]
            self.message = message["message"]
            return self

        except Exception as error:
            return self

    def to_database(self):
        ProtocolDoc(source=self.source, to=self.to,
                    message=self.message, event=self.event).save()
