from flask import Flask
import json
from flask_restful import Api, Resource

from src.database import config_db

from src.documents import ProtocolDoc

app = Flask(__name__)

api = Api(app)


class Mensagens(Resource):
    def get(self, api):
        data = json.loads(ProtocolDoc.objects().to_json())
        print(data)
        return {"data": data}, 200


api.add_resource(Mensagens, "/<api>")
if __name__ == "__main__":
    config_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
