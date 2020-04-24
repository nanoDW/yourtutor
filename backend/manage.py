import click
from flask.cli import FlaskGroup

from backend.app import create_app


def create_backend(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_backend)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create a new admin user
    """
    from backend.extensions import db
    from backend.models import User

    if not User.query.filter_by(email="admin@mail.com").first():
        click.echo("create user")
        user = User(
            email="admin@mail.com", password="admin", active=True, is_admin=True
        )
        db.session.add(user)
        db.session.commit()
        click.echo("created user admin")


if __name__ == "__main__":
    cli()
