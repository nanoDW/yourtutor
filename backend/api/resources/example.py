from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models import Example, User
from backend.extensions import ma, db


def create_path(json_entry):
    return "http://prawo.sejm.gov.pl/isap.nsf/download.xsp/{}/{}/{}".format(
        json_entry["address"],
        json_entry["texts"][0]["type"],
        json_entry["texts"][0]["fileName"],
    )


class ExampleSchema(ma.ModelSchema):
    id = ma.Int(dump_only=True)
    search_query = ma.Str(required=False)
    search_tags = ma.Raw(required=False)
    user_id = ma.Int(required=False)

    class Meta:
        model = Example
        sqla_session = db.session


class ExampleResource(Resource):
    """TUTAJ MOŻESZ PISAĆ DOCSY _ SWAGGER SIĘ SAM OGARNIE - OLEJ
    """

    method_decorators = [jwt_required]

    def get(self, example_id):
        schema = ExampleSchema()
        example = Example.query.get_or_404(example_id)
        return {"example by id": schema.dump(example)}

    def put(self, example_id):
        schema = ExampleSchema(partial=True)
        example = Example.query.get_or_404(example_id)
        example = schema.load(request.json, instance=example)

        db.session.commit()

        return {"msg": "example updated", "example": schema.dump(example)}

    def delete(self, example_id):
        example = Example.query.get_or_404(example_id)
        db.session.delete(example)
        db.session.commit()

        return {"msg": "example deleted"}


class ExampleList(Resource):
    """TUTAJ MOŻESZ PISAĆ DOCSY _ SWAGGER SIĘ SAM OGARNIE - OLEJ
    """

    method_decorators = [jwt_required]
    # Ta linia mówi czy wszystkie metody wymagają auth tokena
    # wywalisz to nie będzie auth tokena - można jwt_required dać jako dekorator
    # metody

    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get_or_404(user_id)
        schema = ExampleSchema(many=True)
        example = schema.dump(user.example)
        return {"example for current user": example}, 200

    def post(self):
        user_id = get_jwt_identity()
        schema = ExampleSchema(partial=True)
        search = schema.load(request.json)
        search.user_id = user_id
        return {"msg": "example updated or sth you will figure it out"}
