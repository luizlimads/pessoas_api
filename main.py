import os
from flask import Flask, jsonify, request
import re
import pymongo

app = Flask(__name__)


@app.route('/home/', methods=['GET'])
def index():
    return "<h1>Hello Worlds</h1>"

@app.route("/q/<busca>",methods=['GET','POST'])
def disp(busca):
    client = pymongo.MongoClient("mongodb+srv://userRead:ZmlwSIDLTtMMPQFX@cluster0.nhq2ivc.mongodb.net/?retryWrites=true&w=majority")
    Database = client.get_database('mongodb')
    Pessoas = Database.Pessoas
    mydoc = Pessoas.find_one({ "_id": int(busca) })
    return mydoc

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)