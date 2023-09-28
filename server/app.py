#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/")
def home():
    return "<h1>Zoo app</h1>"


@app.route("/animal/<int:id>")
def animal_by_id(id):
    animal = Animal.query.get_or_404(id)
    return f"""
        <h2>Animal</h2>
        <ul>
            <li>Name: {animal.name}</li>
            <li>Species: {animal.species}</li>
            <li>Zookeeper: {animal.zookeeper.name}</li>
            <li>Enclosure: {animal.enclosure.environment}</li>
        </ul>
    """


@app.route("/zookeeper/<int:id>")
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get_or_404(id)
    return f"""
        <h2>Zookeeper</h2>
        <ul>
            <li>Name: {zookeeper.name}</li>
            <li>Birthday: {zookeeper.birthday}</li>
            <li>Animals:
                <ul>
                    {"".join(f"<li>{animal}</li>" for animal in zookeeper.animals)}
                </ul>
            </li>
        </ul>
    """


@app.route("/enclosure/<int:id>")
def enclosure_by_id(id):
    enclosure = Enclosure.query.get_or_404(id)
    return f"""
        <h2>Enclosure</h2>
        <ul>
            <li>Environment: {enclosure.environment}</li>
            <li>Open to Visitors: {enclosure.open_to_visitors}</li>
            <li>Animals:
                <ul>
                    {"".join(f"<li>{animal}</li>" for animal in enclosure.animals)}
                </ul>
            </li>
        </ul>
    """


if __name__ == "__main__":
    app.run(port=5555, debug=True)
