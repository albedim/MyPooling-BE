from flasgger import Swagger
from mypooling.configuration.config import app, sql
from mypooling.controller import UserController, RideController, StepController, TripController, FeedbackController
from mypooling.controller.docs.swagger import swagger_config, template

# controllers init
app.register_blueprint(RideController.ride)
app.register_blueprint(StepController.step)
app.register_blueprint(UserController.user)
app.register_blueprint(TripController.trip)
app.register_blueprint(FeedbackController.feedback)

Swagger(app, config=swagger_config, template=template)


def create_app():
    with app.app_context():
        sql.create_all()
    return app


if __name__ == '__main__':
    create_app().run(host="192.168.1.10")