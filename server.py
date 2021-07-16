import paho.mqtt.client as MqttClient

from src.protocolo import Protocol
from src.database import config_db


class Client:
    def __init__(self, url, port, on_message, on_connect, on_disconnect) -> None:
        self.url = url
        self.port = port

        self.client = MqttClient.Client(transport="tcp")

        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.on_disconnect = on_disconnect

    def _connect(self):
        self.client.connect(self.url, self.port)


class Server(Client):
    def __init__(self, url, port):
        Client.__init__(self, url, port, self.on_message,
                        self.on_connect, self.on_disconnect)

    def on_connect(self, client, userData, flags, rc):
        print("conectado")
        self.on_subscribe()

    def on_message(self, client, userData, msg):
        message = msg.payload.decode("utf-8")
        protocol = Protocol().from_json(message)

        if protocol != None and protocol.to == "teste":
            protocol.to_database()
            print(protocol.__dict__)

    def on_disconnect(self, client, userData, rc):
        print("disconectado")

    def on_subscribe(self):
        rc = self.client.subscribe("mesh/Teste/toCloud", qos=0)

    def connect(self):
        self._connect()
        self.client.loop_forever()


if __name__ == "__main__":
    config_db()
    server = Server("192.168.1.10", 1883)
    server.connect()
