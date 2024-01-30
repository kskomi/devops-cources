from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
db = Redis (host="redis2")

@app.route("/")
def hello():
    visitsCounter = db.incr('visitsCounter')
    html = "<H1> Hello!!! </H1>" \
	"<b>Visits: </b>{visits}" \
        "</br>" \
        "<b>HostName: </b>{hostname}" \
	"</br>"

    return html.format(visits=visitsCounter, hostname=os.uname().nodename)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=80)

