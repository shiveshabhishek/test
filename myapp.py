from flask import Flask #Flask is a framework that is used to create web server
from redis import Redis, RedisError #Redis is a datastore
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Welcome {yourname}!</h3>" \
           "<b>Container ID:</b> {hostname}<br/>"
    return html.format(yourname=os.getenv("NAME"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)