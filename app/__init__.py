from flask import Flask

from app.config import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # -----------------------
    # Register Blueprints
    # -----------------------

    from app.routes.main import main
    from app.routes.appointment import appointment
    from app.routes.contact import contact
    from app.routes.doctors import doctors
    from app.routes.services import services

    app.register_blueprint(main)
    app.register_blueprint(appointment)
    app.register_blueprint(contact)
    app.register_blueprint(doctors)
    app.register_blueprint(services)

    return app