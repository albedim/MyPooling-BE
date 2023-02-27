template = {
    "swagger": "2.0",
    "info": {
            "title": "MyPooling API",
        "description": "API for MyPooling",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "",
            "email": "dimaio.albe@gmail.com",
            "url": "",
        },
        "termsOfService": "",
        "version": "1.7.5"
    },
    "basePath": "/api/v_1_7_5",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ]
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}
