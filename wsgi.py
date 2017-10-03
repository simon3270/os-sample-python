from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<html><head><title>My Hello World</head><body>Hello World!</body></html>"

if __name__ == "__main__":
    application.run()
