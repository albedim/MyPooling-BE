
#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the constants
#

class Constants():

    NOT_FOUND: str = "This resource was not found"
    NOT_ENOUGH_PERMISSIONS: str = "You don't have the permissions to perform this action"
    CREATED: str = "Created"
    RIDE_ADDED: str = "{username} ha appena prenotato un tuo passaggio"
    FULL_SLOTS = "You can't add more"
    ALREADY_CREATED = "This resource was already created"
    INVALID_REQUEST: str = "Invalid request"

    EMAIL = "dimaio.albe@gmail.com"
    PASSWORD = "lixfrzouclkjserb"
    FRONTEND_URL = 'http://192.168.1.10:3000/MyPooling-FE'

    WELCOME_EMAIL: str = "Hey {name}! \n Benvenuto nella nostra piattaforma"
    PASSWORD_FORGOTTEN_EMAIL: str = "Hey {name}! \n Ecco il link per recuperare la tua password: " + FRONTEND_URL + "/recovery_password?token={token}"

    PAGE_NOT_FOUND = 'This page was not found. See our documentation: https://albedim.pythonanywhere.com'
    PAGE_METHOD_NOT_ALLOWED = 'Method not allowed. See our documentation: https://albedim.pythonanywhere.com'
    PAGE_UNKNOWN_ERROR = 'Unknown error'
