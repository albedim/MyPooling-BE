import datetime
import os
import random
from flask import jsonify
from resources.rest_service import config


class Constants():
    NOT_FOUND: str = "This resource was not found"
    CREATED: str = "Created"
    INVALID_REQUEST: str = "Invalid request",
    FULL_SLOTS = "You can't add more"
    ALREADY_CREATED = "This resource was already created"
