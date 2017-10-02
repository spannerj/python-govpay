# Import every blueprint file
from python_govpay.views import general
from python_govpay.views import govpay


def register_blueprints(app):
    """Adds all blueprint objects into the app."""
    app.register_blueprint(general.general)
    app.register_blueprint(govpay.govpay)

    # All done!
    app.logger.info("Blueprints registered")
