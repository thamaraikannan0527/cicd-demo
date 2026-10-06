from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Python Docker!"


@app.route("/about")
def about():
    return "This is a sample Python application running inside Docker."


@app.route("/api")
def api():
    return {
        "status": "success",
        "message": "Docker Python API is working"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

