import os

from app.controller.controller import controller_bp

from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(controller_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))