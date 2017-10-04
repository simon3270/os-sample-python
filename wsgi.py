from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<html><head><title>Forked Python Build</title></head><body><h1>Forked My Hello World!</h1>Body text</body></html>"

if __name__ == "__main__":
    application.run()
