from mypooling.configuration.config import app, sql
from mypooling.controller import UserController, RideController, StepController, TripController, FeedbackController
from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils

# controllers init
app.register_blueprint(RideController.ride)
app.register_blueprint(StepController.step)
app.register_blueprint(UserController.user)
app.register_blueprint(TripController.trip)
app.register_blueprint(FeedbackController.feedback)


def create_app():
    with app.app_context():
        sql.create_all()
    return app


@app.errorhandler(404)
def page_not_found(e):
    return Utils.createWrongResponse(False, Constants.PAGE_NOT_FOUND, 404), 404


@app.errorhandler(405)
def page_not_found(e):
    return Utils.createWrongResponse(False, Constants.PAGE_METHOD_NOT_ALLOWED, 405), 405


@app.errorhandler(500)
def page_not_found(e):
    return Utils.createWrongResponse(False, Constants.PAGE_UNKNOWN_ERROR, 500), 500


if __name__ == '__main__':
    create_app().run(host="192.168.1.10")