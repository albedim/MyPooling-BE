from flasgger import Swagger
from flask_jwt_extended import JWTManager
from mypooling.configuration.config import app, sql
from mypooling.controller import \
    UserController, \
    RideController, \
    StepController, \
    TripController, \
    FeedbackController, \
    NotificationController
from mypooling.controller.docs.swagger import swagger_config, template

# controllers init
app.register_blueprint(RideController.ride)
app.register_blueprint(NotificationController.notification)
app.register_blueprint(StepController.step)
app.register_blueprint(UserController.user)
app.register_blueprint(TripController.trip)
app.register_blueprint(FeedbackController.feedback)

# modules init
Swagger(app, config=swagger_config, template=template)
JWTManager(app)


def create_app():
    with app.app_context():
        sql.create_all()
    return app


if __name__ == '__main__':
    create_app().run()