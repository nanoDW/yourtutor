from backend.extensions import db, pwd_context


class User(db.Model):
    """User model
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    examples = db.relationship("Example", backref="user", lazy=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)

    def __repr__(self):
        return "<User %s>" % self.email
