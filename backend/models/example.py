from backend.extensions import db


class Example(db.Model):
    """Example - to be changed
    """

    id = db.Column(db.Integer, primary_key=True)
    search_query = db.Column(db.String(1500), nullable=True)
    search_tags = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, **kwargs):
        super(Example, self).__init__(**kwargs)

    def __repr__(self):
        return "<Example %s>" % self.id
