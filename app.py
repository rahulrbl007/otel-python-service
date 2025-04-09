from flask import flask, jsonify
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor

from opentelemetry_config import configure_tracer

configure_tracer()

FlaskInstrumentor().instrument_app(app)

@app.route("/")

def index():
    return jasonify({"message": "Hello from traced Flask app!"})

@app.route("/health")

def health():
    return jasonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
