from mongoengine import Document
from mongoengine.fields import StringField


class ProtocolDoc(Document):
    source = StringField()
    to = StringField()
    message = StringField()
    event = StringField()

    meta = {"collection": "mensagens"}
