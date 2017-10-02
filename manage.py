from flask_script import Manager
from python_govpay.main import app
import os
# Using Alembic?
# See what extra lines are needed here:
# http://192.168.249.38/gadgets/gadget-api/blob/master/manage.py

manager = Manager(app)


@manager.command
def runserver(port=9999):
    """Run the app using flask server"""

    os.environ["PYTHONUNBUFFERED"] = "yes"
    os.environ["LOG_LEVEL"] = "DEBUG"
    os.environ["COMMIT"] = "LOCAL"
    print('Starting')
    app.run(debug=True, port=int(port))


if __name__ == "__main__":
    manager.run()
