from app import app
from app import db


if __name__ == "__main__":
    with app.app_context():
        app.run()