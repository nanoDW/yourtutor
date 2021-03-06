from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from backend.api.resources.example import ExampleSchema
from backend.extensions import apispec
from backend.api.resources import (
    UserResource,
    UserList,
    ExampleResource,
    ExampleList,
)
from backend.api.resources.user import UserSchema

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(UserResource, "/users/<int:user_id>")
api.add_resource(UserList, "/users")

api.add_resource(ExampleResource, "/example/<int:example_id>")
api.add_resource(ExampleList, "/example")


@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("UserSchema", schema=UserSchema)
    apispec.spec.path(view=UserResource, app=current_app)
    apispec.spec.path(view=UserList, app=current_app)

    apispec.spec.components.schema("FavouriteSchema", schema=ExampleSchema)
    apispec.spec.path(view=ExampleResource, app=current_app)
    apispec.spec.path(view=ExampleList, app=current_app)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints,
    returning correct JSON response with associated
    HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
