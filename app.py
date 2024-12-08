from flask import Flask

import config

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
